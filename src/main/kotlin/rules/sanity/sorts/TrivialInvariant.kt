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
import rules.RuleCheckResult
import rules.dpgraph.SanityCheckNode
import rules.dpgraph.SanityCheckNodeType
import rules.sanity.SanityDPResult
import rules.sanity.*
import solver.SolverResult
import spec.cvlast.CVLCmd
import datastructures.stdcollections.*
import report.RuleAlertReport
import utils.*

object TrivialInvariant :
    SanityCheckSort.FunctionIndependent<RuleCheckResult.Single, CVLCmd.Simple.Assert> {
    override val mode = SanityValues.BASIC

    override val preds: List<SanityCheckNodeType> =
        listOf(SanityCheckNodeType.None)

    override fun getRuleNotificationForResult(solverResult: SolverResult): RuleAlertReport {
        if(solverResult == SolverResult.UNSAT){
            return RuleAlertReport.Warning("The trivial invariant sanity check failed. " +
                "The invariant condition is trivially true - it's verified also without assuming it first, or calling any contract function. " +
                "See ${CheckedUrl.SANITY_TRIVIAL_INVARIANT_CHECKS}")
        }
        val status = when (solverResult) {
            SolverResult.SAT -> "succeeded"
            SolverResult.UNKNOWN -> "did not terminate as expected"
            SolverResult.TIMEOUT -> "timed out"
            SolverResult.SANITY_FAIL,
            SolverResult.UNSAT -> `impossible!`
        }
        return RuleAlertReport.Info("The trivial invariant sanity check $status.")
    }

    /**
     * If the invariant failed it is not trivially true.
     */
    override fun concludeResultFromPredsOrNull(
        predsResults: Map<SanityCheckNode, SanityDPResult>,
    ): SolverResult? {
        predsResults.keys.forEach {
            if (it.type !in preds) {
                throw IllegalArgumentException("trivial invariant check does not depend on ${it.type}")
            }
        }
        /* conclude trivial-invariant check as passing (SAT) (effectively don't perform this check) if
        any of the base rules (there are multi since this is a function-independent check) is not verified (UNSAT) */
        val shouldConclude = predsResults.values.any {
            when (val ruleCheckResult = it.result) {
                is RuleCheckResult.Single -> ruleCheckResult.result != SolverResult.UNSAT
                is RuleCheckResult.Multi -> ruleCheckResult.computeFinalResult() != SolverResult.UNSAT
                is RuleCheckResult.Error -> true
                is RuleCheckResult.Skipped -> true
            }
        }
        return if (shouldConclude) {
            SolverResult.SAT
        } else {
            null
        }
    }
}
