/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY, without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR a PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package verifier

import config.ReportTypes
import datastructures.stdcollections.*
import instrumentation.transformers.GhostSaveRestoreInstrumenter
import kotlinx.coroutines.Deferred
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import log.*
import report.TreeViewReporter
import rules.CompiledRule
import rules.RuleCheckResult
import scene.IScene
import solver.SolverResult
import spec.CVL
import spec.CVLCompiler
import spec.CVLKeywords
import spec.cvlast.*
import spec.rules.IRule
import tac.CallId
import utils.Range
import vc.data.*
import vc.data.TACProgramCombiners.andThen
import verifier.BoundedModelChecker.Companion.copyFunction
import verifier.BoundedModelChecker.Companion.optimize
import verifier.BoundedModelChecker.Companion.toCore
import java.util.concurrent.ConcurrentHashMap

private val logger = Logger(LoggerTypes.BOUNDED_MODEL_CHECKER)

/**
 * An enum of filters on function sequences generated for [BoundedModelChecker].
 *
 * Note that the order of the list is the order in which the filters are checked in the [filter] function, so it should
 * be ordered by how expensive it is to check each filter.
 */
enum class BoundedModelCheckerFilters(private val filter: BoundedModelCheckerFilter, val appliesToChildren: Boolean, val message: String) {
    COMMUTATIVITY(CommutativityFilter, true, "this squence is commutative with another one"),
    FUNCTION_NON_MODIFYING(FunctionNonModifyingFilter, false, "a function doesn't modify the invariant's storage"),
    IDEMPOTENCY(IdempotencyFilter, true, "this sequence contains consecutive calls to an idempotent function"),
    ;

    companion object {
        fun init(
            cvl: CVL,
            scene: IScene,
            compiler: CVLCompiler,
            compiledFuncs: Map<ContractFunction, Pair<CoreTACProgram, CallId>>,
            funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
            funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
            invAssertProgs: Map<CVLInvariant, CoreTACProgram>,
            treeViewReporter: TreeViewReporter
        ) {
            entries.forEach { it.filter.init(cvl, scene, compiler, compiledFuncs, funcReads, funcWrites, invAssertProgs, treeViewReporter) }
        }

        /**
         * Given a [sequence] and the assertion invariant [CoreTACProgram], returns the first [BoundedModelCheckerFilters]
         * that this [sequence] failed to pass, or `null` if the [sequence] passed all filters
         */
        suspend fun filter(
            sequence: List<ContractFunction>,
            inv: CVLInvariant,
            funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
            funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>
        ): BoundedModelCheckerFilters? {
            require(sequence.isNotEmpty())
            return entries.firstOrNull { !it.filter.filter(sequence, inv, funcReads, funcWrites) }
        }
    }
}

private sealed interface BoundedModelCheckerFilter {
    fun init(
        cvl: CVL,
        scene: IScene,
        compiler: CVLCompiler,
        compiledFuncs: Map<ContractFunction, Pair<CoreTACProgram, CallId>>,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        invAssertProgs: Map<CVLInvariant, CoreTACProgram>,
        treeViewReporter: TreeViewReporter
    )

    suspend fun filter(
        sequence: List<ContractFunction>,
        inv: CVLInvariant,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>
    ): Boolean
}

/**
 * If function `f` and `g` only touch disjoint parts of storage and ghosts (read or write), then calling `f->g` and `g->f` are
 * equivalent, so this filters chooses one ordering and filters out all sequences with that order.
 * Note - If there are multiple possible functions in the steps of the sequence, two steps will be commutative if all
 * functions in the first step commute with all functions in the second one.
 */
private data object CommutativityFilter : BoundedModelCheckerFilter {
    /**
     * A function pair in this set is commutative. The [filter] logic will skip sequences where the pair of functions
     * are in the order as it appears in this set, and will pass (keep) sequences where the pair is reversed.
     */
    private lateinit var commutativeFuncs: Set<Pair<ContractFunction, ContractFunction>>

    override fun init(
        cvl: CVL,
        scene: IScene,
        compiler: CVLCompiler,
        compiledFuncs: Map<ContractFunction, Pair<CoreTACProgram, CallId>>,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        invAssertProgs: Map<CVLInvariant, CoreTACProgram>,
        treeViewReporter: TreeViewReporter
    ) {
        val res = mutableSetOf<Pair<ContractFunction, ContractFunction>>()
        val ent = compiledFuncs.keys
            .sortedBy { it.getSighash() } // So for each pair the same ordering will be chosen across runs (useful for testing)
            .withIndex()
            .toList()
        for ((ind1, f1) in ent) {
            for (ind2 in ((ind1+1)..ent.lastIndex)) {
                val f2 = ent[ind2].value

                // If any of the following returns null it means we had a storage analysis failure, and therefore we can't
                // make any assumptions about the commutativity of that function nd we just continue the loop.
                val f1Reads = funcReads[f1] ?: continue
                val f2Reads = funcReads[f2] ?: continue
                val f1Writes = funcWrites[f1] ?: continue
                val f2Writes = funcWrites[f2] ?: continue

                if(
                    f1Reads.overlaps(f2Writes) ||
                    f1Writes.overlaps(f2Reads) ||
                    f1Writes.overlaps(f2Writes)
                ) {
                    continue
                }

                val msg = "The function pair (${f1}, ${f2}) is commutative"
                logger.info { msg }
                res.add(f1 to f2)
            }
        }
        commutativeFuncs = res
        logger.info { "There are ${commutativeFuncs.size} commutative function pairs" }
    }

    override suspend fun filter(
        sequence: List<ContractFunction>,
        inv: CVLInvariant,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>
    ): Boolean {
        return sequence.size < 2 || sequence.zipWithNext { a, b ->
            (a to b) !in commutativeFuncs
        }.all { it }
    }

}

/**
 * Given a function `f`, it is idempotent if the state of storage and ghosts is the same when calling `f()` or `f()->f()`.
 * This filter filters out all sequences where idempotent functions appear twice in a row.
 * Note - If there are multiple possible functions in the steps of the sequence, this will check if there are two consecutive
 * steps that have exactly one function each, and it's the same function.
 */
private data object IdempotencyFilter : BoundedModelCheckerFilter {
    private lateinit var idempotencyCheckProgs: Map<ContractFunction, CoreTACProgram>
    private lateinit var treeViewReporter: TreeViewReporter
    private lateinit var scene: IScene
    private val idempotentFuncs = ConcurrentHashMap<ContractFunction, Deferred<Boolean>>()
    private val parentRule = IRule.createDummyRule("").copy(ruleIdentifier = RuleIdentifier.freshIdentifier("Idempotency checks"))

    override fun init(
        cvl: CVL,
        scene: IScene,
        compiler: CVLCompiler,
        compiledFuncs: Map<ContractFunction, Pair<CoreTACProgram, CallId>>,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        invAssertProgs: Map<CVLInvariant, CoreTACProgram>,
        treeViewReporter: TreeViewReporter
    ) {
        fun ParametricInstantiation<CVLTACProgram>.toOptimizedCoreWithGhostInstrumentation(scene: IScene) =
            this.toCore(scene).let {
                CoreToCoreTransformer(ReportTypes.GHOST_ANNOTATION) { code ->
                    // We need to run this transform again because the storage state save and compare add writes and
                    // reads of ghosts
                    GhostSaveRestoreInstrumenter.transform(code)
                }.transformer(it)
            }.optimize(scene)

        idempotencyCheckProgs = compiledFuncs.entries.toList().mapIndexed { i, (func, funcProg) ->
            val copy1 = funcProg.first.copyFunction()
            val copy2 = funcProg.first.copyFunction()

            val initProg = compiler.generateRuleSetupCode().transformToCore(scene).optimize(scene)

            val saveStorageStateProg = compiler.compileCommands(
                withScopeAndRange(CVLScope.AstScope, Range.Empty()) {
                    listOf(
                        CVLCmd.Simple.Definition(
                            range,
                            CVLType.PureCVLType.VMInternal.BlockchainState,
                            listOf(
                                CVLLhs.Id(
                                    range,
                                    "afterFirst$i",
                                    CVLType.PureCVLType.VMInternal.BlockchainState.asTag()
                                )
                            ),
                            CVLExp.VariableExp(
                                CVLKeywords.lastStorage.keyword,
                                CVLKeywords.lastStorage.type.asTag()
                            ),
                            scope
                        )
                    )
                },
                "check idempotency of $func"
            ).toOptimizedCoreWithGhostInstrumentation(scene)

            val ghostUniverse = cvl.ghosts.filter { !it.persistent }.map {
                StorageBasis.Ghost(it)
            }

            val compareStorageStateProg = compiler.compileCommands(
                withScopeAndRange(CVLScope.AstScope, Range.Empty()) {
                    listOf(
                        CVLCmd.Simple.Assert(
                            range,
                            CVLExp.RelopExp.EqExp(
                                CVLExp.VariableExp(
                                    CVLKeywords.lastStorage.keyword,
                                    CVLKeywords.lastStorage.type.asTag()
                                ),
                                CVLExp.VariableExp(
                                    "afterFirst$i",
                                    CVLKeywords.lastStorage.type.asTag()
                                ),
                                CVLType.PureCVLType.Primitive.Bool.asTag().copy(
                                    annotation = ComparisonType(ComparisonBasis.All(ghostUniverse), false)
                                )
                            ),
                            "not idempotent",
                            scope
                        )
                    )
                },
                "check idempotency of $func"
            ).toOptimizedCoreWithGhostInstrumentation(scene)

            val prog = initProg andThen copy1 andThen saveStorageStateProg andThen copy2 andThen compareStorageStateProg

            func to prog.copy(name = "idempotency of $func")
        }.toMap()

        treeViewReporter.addTopLevelRule(parentRule)
        this.treeViewReporter = treeViewReporter
        this.scene = scene
    }

    private suspend fun computeIdempotency(func: ContractFunction): Boolean {
        val rule = IRule.createDummyRule("").copy(ruleIdentifier = parentRule.ruleIdentifier.freshDerivedIdentifier("$func"))
        treeViewReporter.registerSubruleOf(rule, parentRule)
        treeViewReporter.signalStart(rule)
        val compiledRule = CompiledRule.create(rule, idempotencyCheckProgs[func]!!, treeViewReporter.liveStatsReporter)
        val res = compiledRule.check(scene.toIdentifiers(), true).toCheckResult(scene, compiledRule).getOrElse { RuleCheckResult.Error(compiledRule.rule, it) }
        treeViewReporter.signalEnd(rule, res)

        if (res is RuleCheckResult.Single && res.result == SolverResult.UNSAT) {
            val msg = "The function ${func.methodSignature} is idempotent"
            logger.info { msg }
            return true
        }

        return false
    }

    override suspend fun filter(
        sequence: List<ContractFunction>,
        inv: CVLInvariant,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>
    ): Boolean = coroutineScope {
        sequence.size < 2 || sequence.zipWithNext { a, b ->
            a != b || !idempotentFuncs.computeIfAbsent(a) {
                async { computeIdempotency(a) }
            }.await()
        }.all { it != false }
    }
}

/**
 * If a function doesn't write to any storage/ghost that the invariant's condition accesses, then having it as the last
 * function in a sequence will always return the same result as that sequence without this function at the end, so skip
 * it.
 * Note - Currently the filter just blindly passes sequences where there are multiple possible functions in the last
 * step of the sequence.
 */
private data object FunctionNonModifyingFilter : BoundedModelCheckerFilter {
    /** Mapping of whether a given invariant assertion program and contract function have "interacting" storage or ghosts */
    private lateinit var invAndFuncInteract: Map<Pair<CVLInvariant, ContractFunction>, Boolean>

    private val secondReadsFromFirst = ConcurrentHashMap<Pair<ContractFunction, ContractFunction>, Boolean>()

    override fun init(
        cvl: CVL,
        scene: IScene,
        compiler: CVLCompiler,
        compiledFuncs: Map<ContractFunction, Pair<CoreTACProgram, CallId>>,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        invAssertProgs: Map<CVLInvariant, CoreTACProgram>,
        treeViewReporter: TreeViewReporter
    ) {
        val invAccesses = invAssertProgs.mapValues { (_, assertProg) ->
            val (writes, reads) = BoundedModelChecker.getAllWritesAndReads(assertProg, null)
            writes?.plus(reads)
        }

        invAndFuncInteract = invAccesses.flatMap { (inv, invAccess) ->
            compiledFuncs.map { (func, _) ->
                if (invAccess == null) {
                    return@map (inv to func) to true
                }
                val fWrites = funcWrites[func] ?: return@map (inv to func) to true

                val res = invAccess.overlaps(fWrites)
                if (!res) {
                    val msg = "The function $func doesn't modify the storage accessed by the condition of ${inv.id}"
                    logger.info { msg }
                }
                (inv to func) to res
            }
        }.toMap()
    }

    override suspend fun filter(
        sequence: List<ContractFunction>,
        inv: CVLInvariant,
        funcReads: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>,
        funcWrites: Map<ContractFunction, BoundedModelChecker.Companion.StateModificationFootprint?>
    ): Boolean {
        for (i in sequence.indices.reversed()) {
            val g = sequence[i]
            if (invAndFuncInteract[inv to g]!!) {
                continue
            }
            if (i == sequence.lastIndex) {
                return false
            }

            val readFromG = sequence.subList(i + 1, sequence.size).map { func ->
                secondReadsFromFirst.computeIfAbsent(g to func) {
                    check(g in funcWrites) { "$g not in funcWrites!" }
                    check(func in funcReads) { "$func not in funcReads!" }
                    funcWrites[g]?.overlaps(funcReads[func]) ?: true
                }
            }

            if (readFromG.none { it }) {
                return false
            }
        }
        return true
    }
}
