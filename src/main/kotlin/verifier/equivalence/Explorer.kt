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

import datastructures.NonEmptyList
import instrumentation.transformers.tracing.BufferTraceInstrumentation
import rules.RuleCheckResult
import tac.Tag
import vc.data.CoreTACProgram
import vc.data.TACSymbol
import verifier.AbstractTACChecker

internal class Explorer(
    traceLevel: EquivalenceChecker.InstrumentationLevels,
    context: QueryContext
) : AbstractExplorer(traceLevel, context) {
    override fun generateVC(
        methodAInst: BufferTraceInstrumentation.InstrumentationResults,
        methodBInst: BufferTraceInstrumentation.InstrumentationResults
    ): CoreTACProgram {
        val traceIndex = TACSymbol.Var("traceIndex", Tag.Bit256).toUnique("!")
        return generateVC(traceIndex, methodAInst, methodBInst)
    }

    override fun onTimeout(
        methodA: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodB: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
        pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
    ): EquivalenceChecker.TraceExplorer? {
        return this.traceLevel.onTimeout(
            pairwiseProofManager = pairwiseProofManager,
            aConfig = methodA.instrumentation
        )?.let {
            Explorer(it, context)
        }
    }

    override suspend fun onUnsat(
        methodA: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodB: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
        pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
    ): EquivalenceChecker.UnsatInterpretation {
        traceLevel.onSuccess(methodA.instrumentation, methodB.instrumentation)?.let {
            return EquivalenceChecker.UnsatInterpretation.Refine(Explorer(it, context))
        }
        return EquivalenceChecker.UnsatInterpretation.Verified
    }

    override suspend fun onSat(
        models: NonEmptyList<AbstractTACChecker.ExampleInfo>,
        methodAContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodBContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
        vcProgram: CoreTACProgram,
        failureResult: RuleCheckResult.Single.WithCounterExamples,
        pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
    ): EquivalenceChecker.SatInterpretation {
        return CounterExampleAnalyzer(
            theModel = models.head.model,
            ruleResult = failureResult,
            instLevels = traceLevel,
            vcProgram = vcProgram,
            methodAContext = methodAContext,
            methodBContext = methodBContext,
            context = context,
            pairwiseProofManager = pairwiseProofManager
        ).analyzeCounterExample()
    }
}
