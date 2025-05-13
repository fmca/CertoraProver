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

package rules.genericrulecheckers

import algorithms.transitiveClosure
import algorithms.traverseBFS
import algorithms.traverseBFS1
import analysis.CmdPointer
import analysis.icfg.CVLLabelStack
import analysis.icfg.SummaryStack
import datastructures.stdcollections.*
import log.*
import report.RuleAlertReport
import rules.CompiledRule
import spec.CVLCompiler
import spec.cvlast.SpecType
import tac.NBId
import utils.*
import vc.data.*
import vc.data.tacexprutil.asVar
import vc.data.tacexprutil.isVar

/**
 * A checker generating rule notifications for require statements that do not have a reason string given by the user
 * Will generate a notification for each such require, generally at info level, but instead at warning level if we detect
 * that the require statement affects the possible values of an argument given to a solidity function call, except through summaries.
 */
fun collectRequireWithoutReasonNotifications(compiledRule: CompiledRule): List<RuleAlertReport.Single<*>> {
    if (compiledRule.rule.ruleType is SpecType.Single.GeneratedFromBasicRule.SanityRule) {
        /**
         * We only show the notification for the actual rule, not all derived rules, i.e. rules that are generated in
         * sanity mode ([config.Config.DoSanityChecksForRules]).
         */
        return emptyList()
    }
    val tac = compiledRule.tac

    val graph = tac.analysisCache.graph
    val inverseReachability = lazy { transitiveClosure(graph.blockPred, reflexive = true) }

    fun isRequireWithoutReason(cmd: TACCmd.Simple): Boolean {
        return cmd is TACCmd.Simple.AssumeCmd && TACMeta.CVL_USER_DEFINED_ASSUME in cmd.meta && !cmd.meta[TACMeta.CVL_USER_DEFINED_ASSUME]!!
    }

    /**
     * Heuristic for detecting whether the require statement [cmd] at [ptr] affects a solidity function call argument
     * Since requires discard traces in which they don't hold, this can not only be calls after the require
     * and not only variables directly mentioned in the condition -
     * we must consider variables influencing the value of the condition as being restricted by it,
     * and any uses of such variables as being influenced by the require, as long as they can occur in the same trace.
     * To approximate this (without taking into account path conditions etc), we consider only blocks in the graph
     * that are reachable as successors or predecessors of the require.
     * Within these, we climb up definition sites of the variables occurring in the required condition, collecting them,
     * and then from the definition sites climb down use sites, collecting anything assigned from them as well.
     * We return true if we encounter an annotation that marks being used as a parameter to a solidity call within these uses.
     */
    fun isFunctionInputRequire(cmd: TACCmd.Simple.AssumeCmd, ptr: CmdPointer): Boolean {
        if (!cmd.cond.isVar) {
            return false
        }
        val def = tac.analysisCache.def
        val use = tac.analysisCache.use
        val relevantBlocks = mutableSetOf<NBId>()
        relevantBlocks += tac.analysisCache.reachability[ptr.block].orEmpty()
        relevantBlocks += inverseReachability.value[ptr.block].orEmpty()
        // blocks that are inside summary applications are not to be considered
        val labelStack = CVLLabelStack(graph)
        relevantBlocks.removeIf {
            labelStack.activationRecordsAt(CmdPointer(it, 0)).any { record ->
                record.annot.v is SummaryStack.SummaryStart
            }
        }

        val varsInfluencingCond = mutableSetOf<Pair<TACSymbol.Var, CmdPointer>>()
        traverseBFS1(cmd.cond.asVar to ptr) { (v, p) ->
            val defSites = def.defSitesOf(v, p).filter { it.block in relevantBlocks }
            // we collect them by side effect here since we want the var mapped to its definition site,
            // while the pairs the getReachable itself operates on are variables mapped to their use sites
            // we also want to keep vars for which we could not find a definition site and just consider them as defined from root
            varsInfluencingCond += defSites.map { v to it }.ifEmpty { listOf(v to CmdPointer(tac.rootBlock.id, 0)) }
            defSites.flatMapToSet { cmdPtr ->
                graph.toCommand(cmdPtr).getFreeVarsOfRhs()
                    .filter { it.tag.isPrimitive() }
                    .map { it to cmdPtr }
            }
        }
        traverseBFS(varsInfluencingCond) { (v, p) ->
            val useSites = use.useSitesAfter(v, p).filter { it.block in relevantBlocks }
            useSites.flatMapToSet {
                val (usePtr, useCmd) = graph.elab(it)
                val next = mutableListOf(v to usePtr) // look also at next usages of the same var after this
                when (useCmd) {
                    is TACCmd.Simple.AssigningCmd -> {
                        // consider usages of the assigned var after this point
                        if (useCmd.lhs.tag.isPrimitive()) {
                            next.add(useCmd.lhs to usePtr)
                        }
                    }

                    is TACCmd.Simple.AnnotationCmd -> {
                        if (useCmd.maybeAnnotation(CVLCompiler.Companion.TraceMeta.ExternalArg.META_KEY) != null) {
                            // this annotation tells us that the variable is used as an argument to a solidity call
                            return true
                        }
                    }

                    else -> {}
                }
                next
            }
        }
        return false
    }

    fun locationString(cmd: TACCmd.Simple.AssumeCmd): String {
        // we should actually always have a CVL_RANGE on user defined assumes,
        // just make sure not to print anything weird just in case
        val range = cmd.meta[TACMeta.CVL_RANGE] as? Range.Range
        return range?.let { " at $it" }.orEmpty()
    }

    fun sourceString(cmd: TACCmd.Simple.AssumeCmd): String {
        val range = cmd.meta[TACMeta.CVL_RANGE] as? Range.Range
        return range?.slicedString()?.let { " (`${it}`)" }.orEmpty()
    }

    return graph.commands
        .filter { isRequireWithoutReason(it.cmd) }
        .map { (ptr, cmd) ->
            check(cmd is TACCmd.Simple.AssumeCmd)
            if (isFunctionInputRequire(cmd, ptr)) {
                Logger.regression { "Function-Input-Require${sourceString(cmd)} without Reason${locationString(cmd)}" }
                RuleAlertReport.Warning(
                    "Rule depends on a `require`${sourceString(cmd)} without reason${locationString(cmd)} that affects an argument of a solidity call. " +
                        "Be sure to carefully evaluate whether this `require` may hide relevant behaviors and document it with a reason."
                )
            } else {
                Logger.regression { "Non-Function-Input-Require${sourceString(cmd)} without Reason${locationString(cmd)}" }
                RuleAlertReport.Info(
                    "Rule depends on a `require`${sourceString(cmd)} without reason${locationString(cmd)}. " +
                        "Be sure to carefully evaluate whether this `require` may hide relevant behaviors and document it with a reason."
                )
            }
        }.toList()
}
