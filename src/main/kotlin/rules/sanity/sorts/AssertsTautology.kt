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

object AssertsTautology :
    SanityCheckSort.FunctionDependent<RuleCheckResult.Single, CVLCmd.Simple.Assert> {
    override val mode = SanityValues.ADVANCED

    override val preds: List<SanityCheckNodeType> =
        listOf(SanityCheckNodeType.None)

    override fun getRuleNotificationForResult(solverResult: SolverResult): RuleAlertReport {
        val msg =  "The assert tautology sanity check ${solverResult.toSanityStatusString()}."
        return if(solverResult == SolverResult.UNSAT) {
            RuleAlertReport.Warning(msg + " The respective assert is a tautology, i.e. is always true. See ${CheckedUrl.SANITY_ASSERTS_TAUTOLOGY}")
        } else {
            RuleAlertReport.Info(msg)
        }
    }
    /**
     * If the base rule has failed the assert is not a tautology.
     */
    override fun concludeResultFromPredsOrNull(
        predsResults: Map<SanityCheckNode, SanityDPResult>
    ): SolverResult? {
        require(predsResults.size == 1) { "Expected to have only one predecessor node for an AssertTautology node" }
        val predResult = predsResults.entries.single()
        if (predResult.key.type !in preds) {
            throw IllegalArgumentException("assert-tautology check does not depend on ${predResult.key.type}")
        }
        /* conclude this assert-tautology check as passing (SAT) (effectively don't perform this check) if
        the base rule is not verified (UNSAT) */
        val shouldConclude = when (val ruleCheckResult = predResult.value.result) {
            is RuleCheckResult.Single -> ruleCheckResult.result != SolverResult.UNSAT
            is RuleCheckResult.Multi -> ruleCheckResult.computeFinalResult() != SolverResult.UNSAT
            is RuleCheckResult.Error -> true
            is RuleCheckResult.Skipped -> true
        }
        return if (shouldConclude) {
            SolverResult.SAT
        } else {
            null
        }
    }

}
