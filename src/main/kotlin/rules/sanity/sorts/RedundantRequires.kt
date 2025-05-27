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
import solver.SolverResult
import spec.cvlast.CVLCmd
import datastructures.stdcollections.*
import report.RuleAlertReport
import utils.*

data class RedundantRequires(val assumeCmd: CVLCmd.Simple.AssumeCmd) :
    SanityCheckSort.FunctionDependent<RuleCheckResult.Single, CVLCmd.Simple.AssumeCmd> {
    override val mode = SanityValues.ADVANCED

    override val preds: List<SanityCheckNodeType> =
        listOf(
            SanityCheckNodeType.SanityCheck(AssertsTautology),
            SanityCheckNodeType.SanityCheck(TrivialInvariant)
        )
    override fun getRuleNotificationForResult(solverResult: SolverResult): RuleAlertReport.Single<*> {
        val msg = "The require-redundancy sanity check ${solverResult.toSanityStatusString()}. " +
            if (solverResult == SolverResult.UNSAT) {
                "There are require statements in the rule that are redundant and can be removed. " +
                    "See ${CheckedUrl.SANITY_REDUNDANT_REQUIRES}"
            } else {
                ""
            }
        return RuleAlertReport.Info(msg)
    }
    /**
     * If the asserts are vacuous the require is redundant.
     */
    override fun concludeResultFromPredsOrNull(predsResults: Map<SanityCheckNode, SanityDPResult>): SolverResult? {
        predsResults.keys.forEach {
            if (it.type !in preds) {
                throw IllegalArgumentException("redundant-require check does not depend on ${it.type}")
            }
        }
        /* conclude this redundant-require check as failing (UNSAT) if
        all the predecessors are failing (UNSAT) */
        val shouldConclude = predsResults.values.all {
            when (val ruleCheckResult = it.result) {
                is RuleCheckResult.Single -> ruleCheckResult.result == SolverResult.UNSAT
                is RuleCheckResult.Multi -> ruleCheckResult.computeFinalResult() == SolverResult.UNSAT
                is RuleCheckResult.Error -> false
                is RuleCheckResult.Skipped -> false
            }
        }
        return if (shouldConclude) {
            SolverResult.UNSAT
        } else {
            null
        }
    }
}
