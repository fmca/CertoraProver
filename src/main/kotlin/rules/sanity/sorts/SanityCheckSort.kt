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
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package rules.sanity.sorts

import cli.SanityValues
import report.RuleAlertReport
import rules.RuleCheckResult
import rules.dpgraph.SanityCheckNode
import rules.dpgraph.SanityCheckNodeType
import rules.sanity.SanityDPResult
import rules.sanity.*
import solver.SolverResult
import spec.cvlast.SpecType
import utils.*


/**
 * Represents a sanity check's sort properties, such as how results are grouped,
 * what is the severity of this sort, corresponding UI messages.
 * This class is parametric in the [RuleCheckResult] ([S]) which is the type of the non error [RuleCheckResult]s,
 * and in the atomic sub-check criterion ([G]).
 * An example for an atomic sub-check is redundancy of a specific require (so the require itself is the criterion).
 */
sealed interface SanityCheckSort<in S : RuleCheckResult.Single, G> {

    companion object {

        /**
         * Maps rule type to its corresponding sanity check sort.
         */
        operator fun invoke(type: SpecType.Single.GeneratedFromBasicRule.SanityRule) =
            when (type) {
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.RedundantRequireCheck -> {
                    RedundantRequires(type.assumeCVLCmd)
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.AssertTautologyCheck -> {
                    AssertsTautology
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.TrivialInvariantCheck -> {
                    TrivialInvariant
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.VacuityCheck -> {
                    Vacuity
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.AssertionStructureCheck.LeftOperand-> {
                    AssertionsStructureLeftOperand(type.assertCVLCmd, type.expr)
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.AssertionStructureCheck.RightOperand -> {
                    AssertionsStructureRightOperand(type.assertCVLCmd, type.expr)
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.AssertionStructureCheck.IFFBothTrue -> {
                    AssertionsStructureIFFBothTrue(type.assertCVLCmd, type.expr)
                }
                is SpecType.Single.GeneratedFromBasicRule.SanityRule.AssertionStructureCheck.IFFBothFalse -> {
                    AssertionsStructureIFFBothFalse(type.assertCVLCmd, type.expr)
                }
            }
    }

    val mode: SanityValues

    /**
     * Immediate dependencies (predecessors) of this [SanityCheckSort].
     * These are the rules whose results are required to compute the result
     * of this sanity check.
     */
    val preds: List<SanityCheckNodeType>

    /**
     * Checks if [other] is a predecessor of this sort.
     * Allows dependency check based on sort's properties, for example - two sanity checks that check an assert
     * can be considered dependent only if they check the same assert.
     */
    fun dependsOnOther(
        otherType: SanityCheckNodeType
    ): Boolean = preds.contains(otherType)

    /**
     * Tries to compute the [SolverResult] of this sanity-check's rule ([rule]) from the predecessors' results
     * [predsResults]. Returns null if it is unable to compute the result.
     */
    fun concludeResultFromPredsOrNull(predsResults: Map<SanityCheckNode, SanityDPResult>): SolverResult?

    /**
     * Given the [SolverResult] of the computation generates a Notification that is
     * displayed in the Rule Notifications tab.
     */
    fun getRuleNotificationForResult(solverResult: SolverResult): RuleAlertReport.Single<*>

    /**
     * A sort of sanity-check whose result may change when checked for different methods
     * in the case of parametric rules.
     */
    sealed interface FunctionDependent<S : RuleCheckResult.Single, G> :
        SanityCheckSort<S, G>
    /**
     * A sort of sanity-check whose result can be obtained without checking it separately
     * for each method in the case of parametric rules.
     */
    sealed interface FunctionIndependent<S : RuleCheckResult.Single, G> :
        SanityCheckSort<S, G>

    /**
     * Returns the SolverResult in a human-readable string format that
     * is used for Rule Notifications.
     * Note that the String may depend on the actual sanity check type, i.e., UNSAT
     * may not always mean a failure. Therefore, only use this string representation
     * for creating a rule notification when appropriate.
     */
    fun SolverResult.toSanityStatusString() = when(this){
        SolverResult.UNSAT -> "failed"
        SolverResult.SAT -> "succeeded"
        SolverResult.UNKNOWN -> "did not terminate as expected"
        SolverResult.TIMEOUT -> "timed out"
        SolverResult.SANITY_FAIL -> `impossible!`
    }
}
