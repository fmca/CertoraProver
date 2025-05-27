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
import spec.cvlast.CVLExp
import datastructures.stdcollections.*
import report.RuleAlertReport
import utils.*

val assertionStructurePreds = listOf(SanityCheckNodeType.SanityCheck(Vacuity))

sealed interface AssertionsStructure : SanityCheckSort.FunctionDependent<RuleCheckResult.Single, CVLCmd.Simple.Assert> {
    override val mode
        get() = SanityValues.ADVANCED
    val assertCmd: CVLCmd.Simple.Assert
    val assertExp: CVLExp.BinaryExp
    override val preds: List<SanityCheckNodeType> get() = assertionStructurePreds

    val severityLevel: SanityCheckSeverity
    override fun getRuleNotificationForResult(solverResult: SolverResult): RuleAlertReport.Single<*> {
        val msg = "The assertion structure check of the `require` command at location ${assertCmd.range} ${solverResult.toSanityStatusString()}. See ${CheckedUrl.SANITY_ASSERTIONS_STRUCTURE}\""
        return if(severityLevel is SanityCheckSeverity.Critical && solverResult == SolverResult.UNSAT) {
            RuleAlertReport.Warning(msg)
        } else {
            RuleAlertReport.Info(msg)
        }
    }

    override fun concludeResultFromPredsOrNull(
        predsResults: Map<SanityCheckNode, SanityDPResult>
    ): SolverResult? {
        require(predsResults.size == 1) { "Expected to have only one predecessor for an AssertionStructure node" }
        val predResult = predsResults.entries.single()
        if (predResult.key.type !in preds) {
            throw IllegalArgumentException("assertion-structure check does not depend on ${predResult.key.type}")
        }
        /* conclude this check as failing (UNSAT) if
        vacuity check is failing */
        val shouldConclude = when (val ruleCheckResult = predResult.value.result) {
            is RuleCheckResult.Single -> ruleCheckResult.result == SolverResult.UNSAT
            is RuleCheckResult.Multi -> ruleCheckResult.computeFinalResult() == SolverResult.UNSAT
            is RuleCheckResult.Error -> false
            is RuleCheckResult.Skipped -> false
        }
        return if (shouldConclude) {
            SolverResult.UNSAT
        } else {
            null
        }
    }
}

class AssertionsStructureLeftOperand(override val assertCmd: CVLCmd.Simple.Assert, override val assertExp: CVLExp.BinaryExp) : AssertionsStructure {
    override val severityLevel: SanityCheckSeverity
        get() = if (assertExp is CVLExp.BinaryExp.ImpliesExp) {
            SanityCheckSeverity.Critical
        } else {
            SanityCheckSeverity.Info
        }

}

class AssertionsStructureRightOperand(override val assertCmd: CVLCmd.Simple.Assert, override val assertExp: CVLExp.BinaryExp) : AssertionsStructure {
    override val severityLevel: SanityCheckSeverity
        get() = SanityCheckSeverity.Info
}

class AssertionsStructureIFFBothFalse(override val assertCmd: CVLCmd.Simple.Assert, override val assertExp: CVLExp.BinaryExp) : AssertionsStructure {
    override val severityLevel: SanityCheckSeverity
        get() = SanityCheckSeverity.Info


}

class AssertionsStructureIFFBothTrue(override val assertCmd: CVLCmd.Simple.Assert, override val assertExp: CVLExp.BinaryExp) : AssertionsStructure {
    override val severityLevel: SanityCheckSeverity
        get() = SanityCheckSeverity.Info

    override val preds: List<SanityCheckNodeType>
        get() = listOf(SanityCheckNodeType.SanityCheck(AssertionsStructureIFFBothFalse(assertCmd, assertExp)))

    override fun concludeResultFromPredsOrNull(
        predsResults: Map<SanityCheckNode, SanityDPResult>
    ): SolverResult? {
        require(predsResults.size <= 1) {"assertion structure check for $assertExp should have only one predecessor"}
        if (predsResults.isEmpty()) {
            return null
        }
        val predResult = predsResults.entries.single()
        if (!preds.contains(predResult.key.type)) {
            throw IllegalArgumentException("assert-structure check for $assertExp does not depend on " +
                    "${predResult.key.type}")
        }
        return when (val firstResult = predResult.value.result) {
            is RuleCheckResult.Error -> null
            is RuleCheckResult.Multi -> {
                if (firstResult.computeFinalResult() == SolverResult.UNSAT) {
                    SolverResult.SAT
                } else {
                    null
                }
            }

            is RuleCheckResult.Single -> {
                if (firstResult.result == SolverResult.UNSAT) {
                    SolverResult.SAT
                } else {
                    null
                }
            }

            is RuleCheckResult.Skipped -> null
        }
    }

}
