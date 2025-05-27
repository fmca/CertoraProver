/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package verifier.equivalence.summarization

import analysis.*
import analysis.ip.INTERNAL_FUNC_EXIT
import analysis.ip.INTERNAL_FUNC_START
import analysis.ip.InternalFunctionExitFinder
import analysis.opt.ConstantComputationInliner
import analysis.opt.PointerSimplification
import com.certora.collect.*
import compiler.SolidityFunctionStateMutability
import datastructures.stdcollections.*
import instrumentation.transformers.TACDSA
import scene.IContractWithSource
import scene.TACMethod
import spec.cvlast.QualifiedMethodSignature
import spec.cvlast.SolidityContract
import spec.cvlast.Visibility
import spec.cvlast.typedescriptors.VMValueTypeDescriptor
import tac.MetaKey
import tac.Tag
import utils.*
import vc.data.*
import java.util.stream.Collectors

/**
 * Extract "common" pure internal functions from a method. These are pure (as annotated in the original
 * source code and checked by the compiler) functions which appear one or more times within a given method.
 * For one of these functions F, this class determines whether all instances of F have some unified, canonical
 * representation, and if so, what the canonical representation is.
 */
object PureFunctionExtraction {

    /**
     * An instance of a canonicalized function with signature [qual] which starts at [where].
     *
     * The canonicalized program is given in [subProgram].
     *
     * [argSyms] and [exitVars] are the canonicalized argument and return values respectively.
     *
     * NB that [argSyms] is [TACSymbol]: if [qual] is called with a constant argument, that constant argument
     * may (or may not) be reflected in the corresponding slot in [argSyms].
     */
    private data class CanonicalizedFunction(
        val qual: QualifiedMethodSignature,
        val where: LTACCmd,
        val argSyms: List<TACSymbol>,
        val exitVars: List<TACSymbol.Var>,
        val subProgram: SimpleCanonicalization.CanonProgramWithMeta,
    )

    /**
     * A dummy annotation intended to keep the exit variables of a program alive to prevent their removal by dead assignment
     * elimination optimizations at the like.
     */
    @KSerializable
    @Treapable
    private data class KeepAlive(
        val list: List<TACSymbol.Var>
    ) : WithSupport, AmbiSerializable {
        override val support: Set<TACSymbol.Var>
            get() = list.toSet()
    }

    private val keepAliveMeta = MetaKey<KeepAlive>("keep.alive")

    /**
     * An inclusion predicate used to select which commands are included by [SimpleCanonicalization].
     */
    private fun canonicalizationInclusionPredicate(lc: LTACCmd) : Boolean {
        return when(lc.cmd) {
            is TACCmd.Simple.AnnotationCmd,
            is TACCmd.Simple.LabelCmd,
            is TACCmd.Simple.SummaryCmd,
            is TACCmd.Simple.JumpdestCmd,
            is TACCmd.Simple.JumpCmd,
            TACCmd.Simple.NopCmd -> false
            is TACCmd.Simple.LogCmd,
            is TACCmd.Simple.AssertCmd,
            is TACCmd.Simple.AssigningCmd,
            is TACCmd.Simple.Assume,
            is TACCmd.Simple.ByteLongCopy,
            is TACCmd.Simple.CallCore,
            is TACCmd.Simple.JumpiCmd,
            is TACCmd.Simple.ReturnCmd,
            is TACCmd.Simple.ReturnSymCmd,
            is TACCmd.Simple.RevertCmd,
            is TACCmd.Simple.WordStore -> true
        }
    }

    /**
     * Represents one or more [CanonicalizedFunction] which all have the exact same canonicalized body
     * (as determined by comparing the [SimpleCanonicalization.ICanonProgram.block] and [SimpleCanonicalization.ICanonProgram.code]
     * of the [equivClass]) and the same [argsSyms] and [exitSyms]. In other words, all [CanonicalizedFunction] which
     * have exactly the same [CanonicalizedFunction.subProgram] and [CanonicalizedFunction.argSyms] and [CanonicalizedFunction.exitVars]
     * are grouped together in an [EquivalenceClass], with a representative [equivClass].
     *
     * Intuitively, this class represents "all bodies of a function called with the same combination of constant/non-constant args"
     *
     * NB that if multiple [CanonicalizedFunction] are grouped together with a variable at some index `i`
     * within [CanonicalizedFunction.argSyms], that doesn't mean the argument *values* at position `i` are the same,
     * simply that all of those instances had *some* symbolic argument at position i.
     */
    private data class EquivalenceClass(
        val equivClass: SimpleCanonicalization.CanonProgramWithMeta,
        val argsSyms: List<TACSymbol>,
        val exitSyms: List<TACSymbol.Var>
    ) {
        fun includes(other: CanonicalizedFunction) : Boolean {
            return equivClass.canon == other.subProgram.canon && this.argsSyms == other.argSyms && this.exitSyms == other.exitVars
        }
    }

    /**
     * Given a canonical representation of some [EquivalenceClass], run some optimizations and then recanonicalize
     * the function. The canonical program in [f] is translated into a [CoreTACProgram] via the [SimpleCanonicalization.CanonProgramWithMeta.toProgram].
     *
     * The optimizations applied to this program are [TACDSA], [ConstantComputationInliner], and [PointerSimplification].
     * The commands in [prefix] are appended to the materialized canonicalized program before any of these
     * optimizations are run.
     */
    private fun optimizeAndRecanonicalize(f: EquivalenceClass, prefix: List<TACCmd.Simple> = listOf()): SimpleCanonicalization.CanonProgram {
        val meta = TACCmd.Simple.AnnotationCmd(
            keepAliveMeta,
            KeepAlive(f.exitSyms)
        )
        val r = f.equivClass.toProgram("test").prependToBlock0(prefix).appendToSinks(CommandWithRequiredDecls(meta))
        return TACDSA.simplify(r, protectedVars = setOf(), protectCallIndex = setOf(), annotate = false, isTypechecked = true)
            .let(ConstantComputationInliner::rewriteConstantCalculations)
            .let(PointerSimplification::simplify)
            .let {
                SimpleCanonicalization.canonicalize(
                    it,
                    start = CmdPointer(it.entryBlockId, 0),
                    forceVariableEquiv = listOf(),
                    end = { _ ->  false },
                    excludeStart = false,
                    include = ::canonicalizationInclusionPredicate
                )
            }.canon
    }


    /**
     * Given multiple [CanonicalizedFunction] instances with the same signature,
     * attempt to extract their canonical representation.
     *
     * Roughly, all of the [CanonicalizedFunction] are grouped into [EquivalenceClass]
     * based on the criteria described there. If we have a single equivalence class,
     * then we are done and select that [EquivalenceClass.equivClass]'s as the canonical
     * representation.
     *
     * If there are multiple possible groups, we try two strategies.
     *
     * First, we heuristically identify if one of the equivalence classes has the most general form:
     * this is the equivalence class with the most symbolic (variable) inputs. Call this equivalence
     * class G. We then check whether all of the remaining classes are simply specializations of G due to constant inlining.
     * Specifically, we check whether all other equivalence classes have constants c1, c2, ... as arguments where G has
     * variables v1, v2, ... Let C be one such equivalence class. We compute `G[c1/v1, c2/v2,...]`, and then check to see whether
     * the simplification and recanonicalization of `G[c1/v1,c2/v2,...]` matches C. If this check succeeds, we conclude that
     * G is the most general, canonical form of the function.
     *
     * If the above process fails, we check if the different function bodies were just optimized differently. We do
     * this by simply reoptimizing and recanonicalizing (via [optimizeAndRecanonicalize]) all the equivalence classes
     * and then checking whether this yields a single result. If so, we return that unique result.
     *
     * Otherwise, we return null, indicating we could not infer a unique, canonical representation for all functions in [canoned].
     */
    private fun canonicalizeGroup(
        canoned: List<CanonicalizedFunction>
    ) : SimpleCanonicalization.CanonProgram? {
        val equiv = mutableListOf<EquivalenceClass>()
        for(p in canoned) {
            if(equiv.any { it.includes(p) }) {
                continue
            }
            equiv.add(EquivalenceClass(
                argsSyms = p.argSyms,
                exitSyms = p.exitVars,
                equivClass = p.subProgram
            ))
        }

        /**
         * Easy case, only one equivalence class, we can call this the canonical representation of this
         * function (within some external method body).
         */
        if(equiv.size == 1) {
            return equiv.single().equivClass.canon
        }

        /**
         * What is the most symbolic arguments?
         */
        val mostVars = equiv.maxOf { repr ->
            repr.argsSyms.count { sym -> sym is TACSymbol.Var }
        }

        /**
         * Is there a single equivalence class with that count?
         */
        val mostGeneralForm = equiv.singleOrNull { eq ->
            eq.argsSyms.count { sym ->
                sym is TACSymbol.Var
            } == mostVars
        }

        /**
         * If not, we fallback here on the "maybe things were just optimized differently" check,
         * by simply re-optimizing and re-canonicalizing every equivalence class,
         * and crossing our fingers this gives a unique result.
         */
        if(mostGeneralForm == null) {
            // one last try
            return equiv.map {
                optimizeAndRecanonicalize(it)
            }.uniqueOrNull()
        }
        /**
         * Otherwise, see if the other equivalence classes are just specializations of mostGeneralForm
         */
        for(eq in equiv) {
            if(eq.equivClass.canon == mostGeneralForm.equivClass.canon) {
                continue
            }
            if(eq.argsSyms.size != mostGeneralForm.argsSyms.size) {
                return null
            }
            val zipped = mostGeneralForm.argsSyms.zip(eq.argsSyms)

            /**
             * This prefix is passed to [optimizeAndRecanonicalize] for the general form, and effects the
             * assignment of constant arguments of `eq` to the symbolic arguments in `mostGeneralForm`.
             *
             */
            val assignPrefix = mutableListOf<TACCmd.Simple>()
            /**
             * In the following `l` is the `mostGeneralForm` argument, and `r` is the argument used
             * in `eq`.
             */
            for((l, r) in zipped) {
                /**
                 * If `eq` and `mostGeneralForm` agree on this argument, skip
                 */
                if(l == r) {
                    continue
                }
                /**
                 * If the disagree on the name of the argument, this is unrecoverable, and
                 * we give up
                 */
                if(l is TACSymbol.Var && r is TACSymbol.Var) {
                    return null
                }
                /**
                 * If `mostGeneralForm` had a constant where `eq` has a variable OR a different constant,
                 * that is also unrecoverable.
                 */
                if(l is TACSymbol.Const) {
                    return null
                }
                /**
                 * you can convince yourself that the following must succeed: l is not a constant (and is
                 * thus a variable) and r is not a variable (otherwise the above `return null` would fire)
                 * and thus must be a constant.
                 */
                check(l is TACSymbol.Var && r is TACSymbol.Const) {
                    "Broken type hierarchy: $l vs $r"
                }
                /**
                 * Assign the constant used in `eq` to the symbolic argument used in `mostGeneralForm`.
                 */
                assignPrefix.add(
                    TACCmd.Simple.AssigningCmd.AssignExpCmd(
                        lhs = l,
                        rhs = r.asSym()
                    )
                )
            }
            /**
             * Recanonicalize `mostGeneralForm` using these constant assignments, which will be folded into the body of
             * the function by [ConstantComputationInliner] used by the [optimizeAndRecanonicalize].
             */
            val newCanon1 = optimizeAndRecanonicalize(mostGeneralForm, assignPrefix)

            /**
             * optimize and recanonicalize. We need to do this here because due canonicalization, the optimizations
             * done in [optimizeAndRecanonicalize] can still make non-trivial changes unrelated to the constant
             * prefix. Thus, we need those same "unrelated to constant arguments" optimizations to be applied
             * to `eq` for an apples to apples comparison.
             */
            val newCanon2 = optimizeAndRecanonicalize(eq, listOf())
            /**
             * Well, even after this, we still do not have a match. give up
             */
            if(newCanon1 != newCanon2) {
                return null
            }
        }
        return mostGeneralForm.equivClass.canon
    }

    /**
     * Indicates that all instances of [sig] within some external program have a canonical representation of
     * [prog]. NB this comes with some caveats, given the handling of specialization described in [canonicalizeGroup]
     */
    data class CanonFunction(
        val sig: QualifiedMethodSignature,
        val prog: SimpleCanonicalization.CanonProgram
    )

    /**
     * Given a set of [pureInternalSigs] that are expected to appear in [prog],
     * compute which can be assigned a canonical representation as represented by the [CanonFunction]
     * objects in the returned list.
     */
    private fun findCanonicalRepresentationFor(
        prog: CoreTACProgram,
        pureInternalSigs: Collection<QualifiedMethodSignature>
    ) : List<CanonFunction> {
        val exits = InternalFunctionExitFinder(prog)
        val mca = MustBeConstantAnalysis(
            graph = prog.analysisCache.graph
        )
        val canoned = prog.parallelLtacStream().mapNotNull {
            it `to?` it.maybeAnnotation(INTERNAL_FUNC_START)
        }.filter { (_, start) ->
            pureInternalSigs.any {
                it.matchesNameAndParams(start.methodSignature)
            }
        }.map { (where, start) ->
            val funcExits = exits.getExits(calleeId = start.id, startPtr = where.ptr)
            val equivs = mutableListOf<MutableSet<TACSymbol.Var>>()
            /**
             * For all exit sites, ensure the variables assigned to the exit variables are given the same canonical name.
             *
             * This is *technically* unsound, as seen in the following example:
             *
             * ```
             * r4 = 3
             * r2 = 5
             * if(*) {
             *    return r4
             * } else {
             *    return r2
             * }
             * ```
             *
             * by unifying `r2` and `r4` we will get:
             * ```
             * V1 = 3
             * V1 = 5
             * if(*) {
             *    return V1
             * } else {
             *    return V1
             * }
             * ```
             *
             * However, this sort of variable reuse is not expected in practice thanks to DSA.
             */
            for(exit in funcExits) {
                for((ind, r) in exit.wrapped.maybeAnnotation(INTERNAL_FUNC_EXIT)!!.rets.withIndex()) {
                    if(ind >= equivs.size) {
                        equivs.add(mutableSetOf())
                    }
                    equivs[ind].add(r.s)
                }
            }
            /**
             * Canonicalize the function body
             */
            val canon = SimpleCanonicalization.canonicalize(
                prog,
                where.ptr,
                excludeStart = true,
                forceVariableEquiv = equivs,
                include = ::canonicalizationInclusionPredicate
            ) { maybeExit ->
                maybeExit.maybeAnnotation(INTERNAL_FUNC_EXIT)?.id == start.id
            }
            val exitVars = equivs.map { repr ->
                canon.variableMapping(repr.first())!!
            }

            val argVars = start.args.mapIndexed { idx, internalArg ->
                when(val a = internalArg.s) {
                    is TACSymbol.Const -> a
                    is TACSymbol.Var -> {
                        canon.variableMapping(a) ?: mca.mustBeConstantAt(
                            where.ptr, a
                        )?.asTACSymbol() ?: TACSymbol.Var("certora!Unused$idx", Tag.Bit256)
                    }
                }
            }
            CanonicalizedFunction(
                where = where,
                argSyms = argVars,
                exitVars = exitVars,
                subProgram = canon,
                qual = start.methodSignature
            )
        }.collect(Collectors.groupingBy {
            it.qual.qualifiedMethodName to it.qual.paramTypes
        })

        /**
         * canoned now holds all of the [CanonicalizedFunction] grouped by signature. For each such
         * group, try to extract the canonical representation via [canonicalizeGroup]
         */
        val toRet = mutableListOf<CanonFunction>()
        for((_, subFuncs) in canoned) {
            val repr = canonicalizeGroup(subFuncs) ?: continue
            toRet.add(
                CanonFunction(
                    sig = subFuncs.first().qual,
                    prog = repr
                )
            )
        }
        return toRet
    }

    /**
     * Within [m], find internal functions which are:
     * 1. Pure (according to the solidity annotation)
     * 2. Have only scalar input/output types
     * 3. Have some canonical representation.
     */
    fun canonicalPureFunctionsIn(m: TACMethod) : List<CanonFunction> {
        val src = (m.getContainingContract() as? IContractWithSource)?.src ?: return listOf()
        val prog = m.code as CoreTACProgram
        val res = prog.parallelLtacStream().mapNotNull {
            it.maybeAnnotation(INTERNAL_FUNC_START)?.methodSignature
        }.filter { sig ->
            sig.paramTypes.all {
                it is VMValueTypeDescriptor
            } && sig.resType.all {
                it is VMValueTypeDescriptor
            } && src.internalFunctions.any { (_, m) ->
                m.method.toMethodSignature(SolidityContract(m.declaringContract), Visibility.INTERNAL).matchesNameAndParams(sig) && m.method.stateMutability == SolidityFunctionStateMutability.pure
            }
        }.collect(Collectors.toSet())
        return findCanonicalRepresentationFor(
            prog, res
        )
    }
}
