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

package verifier.equivalence

import allocator.Allocator
import analysis.CommandWithRequiredDecls
import datastructures.stdcollections.*
import verifier.equivalence.tracing.BufferTraceInstrumentation
import tac.MetaMap
import tac.Tag
import utils.letIf
import vc.data.*
import vc.data.TACProgramCombiners.andThen
import vc.data.codeFromCommandWithVarDecls
import vc.data.tacexprutil.ExprUnfolder

/**
 * Basic [verifier.equivalence.EquivalenceChecker.TraceExplorer] which generates an assertion
 * on traces, and instruments the two programs according to the current [traceLevel] and
 * [verifier.equivalence.EquivalenceChecker.PairwiseProofManager].
 */
internal abstract class AbstractExplorer(
    protected val traceLevel: EquivalenceChecker.IInstrumentationLevels,
    override val context: QueryContext
) : EquivalenceChecker.TraceExplorer, WithQueryContext {

    override fun getAConfig(pairwiseProofManager: EquivalenceChecker.PairwiseProofManager): BufferTraceInstrumentation.InstrumentationControl =
        BufferTraceInstrumentation.InstrumentationControl(
            traceMode = traceLevel.getAInclusion(),
            eventLoggingLevel = traceLevel.traceLevel,
            useSiteControl = pairwiseProofManager.getAUseSiteControl(),
            forceMloadInclusion = pairwiseProofManager.getAMloadOverrides(),
            eventSiteOverride = pairwiseProofManager.getAOverrides()
        )

    override fun getBConfig(pairwiseProofManager: EquivalenceChecker.PairwiseProofManager): BufferTraceInstrumentation.InstrumentationControl =
        BufferTraceInstrumentation.InstrumentationControl(
            traceMode = traceLevel.getBInclusion(),
            eventLoggingLevel = traceLevel.traceLevel,
            useSiteControl = pairwiseProofManager.getBUseSiteControl(),
            forceMloadInclusion = pairwiseProofManager.getBMloadOverrides(),
            eventSiteOverride = pairwiseProofManager.getBOverrides()
        )

    /**
     * Asserts that the traces for [traceLevel] are equal at [traceIndex], using
     * the instrumentation data in [methodAInst] and [methodBInst]. If [traceIndex] is havoced, this is effectively
     * asserting traces are equal. However, callers (namely [TraceMinimizer]) can add constraints to narrow this check.
     *
     * If [traceLevel] is for [BufferTraceInstrumentation.TraceTargets.Results],
     * this also generates an assertion of storage equality.
     */
    protected fun generateVC(
        traceIndex: TACSymbol.Var,
        methodAInst: BufferTraceInstrumentation.InstrumentationResults,
        methodBInst: BufferTraceInstrumentation.InstrumentationResults
    ): CoreTACProgram {
        val getter = traceLevel.traceLevel.loggerExtractor

        val traceValueA = TACSymbol.Var("traceValueA", Tag.Bit256).toUnique("!")
        val traceValueB = TACSymbol.Var("traceValueB", Tag.Bit256).toUnique("!")
        val assertSym = TACSymbol.Var("assertionSym", Tag.Bool).toUnique("!")
        val extractA = methodAInst.traceVariables.getter().getRepresentative(traceIndex)
        val extractB = methodBInst.traceVariables.getter().getRepresentative(traceIndex)

        val assertionFragment = extractA.toCRD() andThen extractB.toCRD() andThen CommandWithRequiredDecls(
            listOf(
                TACCmd.Simple.AnnotationCmd(
                    EquivalenceChecker.IndexHolder.META_KEY, EquivalenceChecker.IndexHolder(
                        indexSym = traceLevel.traceLevel.indexHolder(traceIndex)
                    )
                ),
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = traceValueA,
                    rhs = extractA.exp,
                ),
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = traceValueB,
                    rhs = extractB.exp,
                ),
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = assertSym,
                    rhs = TACExprFactTypeCheckedOnlyPrimitives {
                        (traceValueA eq traceValueB) or if (traceLevel.traceLevel != BufferTraceInstrumentation.TraceTargets.Results) {
                            methodAInst.traceVariables.isRevertingPath or methodBInst.traceVariables.isRevertingPath
                        } else {
                            TACSymbol.False
                        }
                    }
                ),
                TACCmd.Simple.AssertCmd(assertSym,
                    "traces equal",
                    MetaMap(TACMeta.CVL_USER_DEFINED_ASSERT) + (EquivalenceChecker.TRACE_EQUIVALENCE_ASSERTION to traceLevel.traceLevel.ordinal)
                )
            ),
            setOf(
                traceIndex,
                traceValueA,
                traceValueB,
                assertSym,
                methodAInst.traceVariables.isRevertingPath,
                methodBInst.traceVariables.isRevertingPath
            )
        ).letIf(traceLevel.traceLevel == BufferTraceInstrumentation.TraceTargets.Results) { traceAssert ->
            val skolemInd = TACKeyword.TMP(Tag.Bit256, "!storageIdx")
            val reprA = TACKeyword.TMP(Tag.Bit256, "storageValA")
            val reprB = TACKeyword.TMP(Tag.Bit256, "storageValB")
            val storageA = methodA.getContainingContract().storage.stateVars().single()
            val storageB = methodB.getContainingContract().storage.stateVars().single()
            val storageAssert = CommandWithRequiredDecls(
                listOf(
                    TACCmd.Simple.AssigningCmd.WordLoad(
                        lhs = reprA,
                        base = storageA,
                        loc = skolemInd
                    ),
                    TACCmd.Simple.AssigningCmd.WordLoad(
                        lhs = reprB,
                        base = storageB,
                        loc = skolemInd
                    )
                )
            ) andThen ExprUnfolder.unfoldPlusOneCmd("storageEq", TACExprFactoryExtensions.run {
                reprA eq reprB
            }) {
                TACCmd.Simple.AssertCmd(
                    it.s,
                    "storage equal post execution",
                    MetaMap(EquivalenceChecker.STORAGE_EQUIVALENCE_ASSERTION to EquivalenceChecker.StorageComparison(
                        contractAValue = reprA,
                        contractBValue = reprB,
                        skolemIndex = skolemInd
                    ))
                )
            }.merge(skolemInd, reprA, reprB, storageA, storageB)
            traceAssert andThen storageAssert
        }
        return codeFromCommandWithVarDecls(Allocator.getNBId(), assertionFragment, "finalAssertions")
    }
}
