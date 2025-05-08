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
import log.*
import rules.RuleCheckResult
import tac.Tag
import vc.data.*
import vc.data.tacexprutil.ExprUnfolder
import verifier.AbstractTACChecker
import java.math.BigInteger

private val logger = Logger(LoggerTypes.EQUIVALENCE)

/**
 * An [AbstractExplorer] which makes the same assertion as [Explorer], but requires the mismatch to occur before [idx].
 * If this is not possible, then the original counter example we're trying to minimize is further procesed via [continuation].
 */
internal class TraceMinimizer(
    val idx: BigInteger,
    traceLevel: EquivalenceChecker.InstrumentationLevels,
    context: QueryContext,
    val continuation: CounterExampleAnalyzer.CEXContinuation,
) : AbstractExplorer(traceLevel, context) {
    override fun generateVC(
        methodAInst: BufferTraceInstrumentation.InstrumentationResults,
        methodBInst: BufferTraceInstrumentation.InstrumentationResults
    ): CoreTACProgram {
        logger.info {
            "Attempting to find violating trace of length less than $idx"
        }
        val traceVar = TACSymbol.Var("traceIdx", Tag.Bit256)
        val vcProg = generateVC(traceVar, methodAInst, methodBInst)

        val prefix = ExprUnfolder.unfoldPlusOneCmd("assumeMinimal", TACExprFactTypeCheckedOnlyPrimitives {
            traceVar lt idx.asTACExpr
        }) {
            TACCmd.Simple.AssumeCmd(it.s, "trace smaller than $idx")
        }
        return vcProg.prependToBlock0(prefix)
    }

    override suspend fun onSat(
        models: NonEmptyList<AbstractTACChecker.ExampleInfo>,
        methodAContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodBContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
        vcProgram: CoreTACProgram,
        failureResult: RuleCheckResult.Single.WithCounterExamples,
        pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
    ): EquivalenceChecker.SatInterpretation {
        /**
         * Found a smaller trace, analyze that one
         */
        val analyzer = CounterExampleAnalyzer(
            methodBContext = methodBContext,
            methodAContext = methodAContext,
            vcProgram = vcProgram,
            instLevels = traceLevel,
            ruleResult = failureResult,
            theModel = models.head.model,
            context = context,
            pairwiseProofManager = pairwiseProofManager
        )
        return analyzer.analyzeCounterExample()
    }

    override suspend fun onUnsat(
        methodA: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodB: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
        pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
    ): EquivalenceChecker.UnsatInterpretation {
        return EquivalenceChecker.UnsatInterpretation.Override(continuation.resume())
    }

    override fun onTimeout(
        methodA: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodB: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
        pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
    ): EquivalenceChecker.TraceExplorer? {
        return null
    }
}
