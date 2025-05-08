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

package wasm.transform

import datastructures.stdcollections.*
import analysis.PatternDSL
import analysis.PatternMatcher
import analysis.PatternMatcher.Pattern
import analysis.PatternMatcher.Pattern.Companion.toBuildable
import analysis.maybeNarrow
import instrumentation.transformers.removeUnusedAssignments
import utils.*
import vc.data.*
import vc.data.SimplePatchingProgram.Companion.patchForEach
import java.math.BigInteger

/**
 * Simplification of WASM branch conditions. After the initial conversion to TAC, we may have code like:
 *
 * B := <a boolean expression>
 * R := B ? 1 : 0
 * B' := R == 0
 * JMPi B' ...
 *
 * which can be simplified to
 *
 * B := <a boolean expression>
 * B' := LNot B
 * JMPi B'
 *
 *
 * This overlaps somewhat with [BoolOptimizer], but that module only transforms unrolled programs.
 */
object BranchConditionSimplifier {
    /** The different patterns we can recognize */
    sealed interface Rewrite {
        fun rewriteJump(cmd: TACCmd.Simple.JumpiCmd): TACCmd.Simple.JumpiCmd

        /* The condition variable is true when LNot [b] is true */
        data class NegatedVar(val b: TACSymbol.Var): Rewrite {
            override fun rewriteJump(cmd: TACCmd.Simple.JumpiCmd): TACCmd.Simple.JumpiCmd =
                cmd.copy(cond = b, dst = cmd.elseDst, elseDst = cmd.dst)

        }

        /* The condition variable is true when [b] is true */
        data class DoubleNegatedVar(val b: TACSymbol.Var): Rewrite {
            override fun rewriteJump(cmd: TACCmd.Simple.JumpiCmd): TACCmd.Simple.JumpiCmd =
                cmd.copy(cond = b)
        }
    }

    // Matches Var ? 1 : 0
    private fun<R> boolToInt(p: Pattern<R>) = Pattern.Ite(
        p,
        Pattern.FromConstant.exactly(BigInteger.ONE),
        Pattern.FromConstant.exactly(BigInteger.ZERO),
    ) { _,v,_,_ -> v }

    // Matches `LNot (Var ? 1 : 0) == 0`
    private val doubleNegated = PatternDSL.build {
        val negated = Pattern.FromUnaryOp(
            extractor = { _, u -> ((u as? TACExpr.UnaryExp.LNot)?.o as? TACExpr.Sym)?.s },
            inner = boolToInt(Pattern.FromVar.anyVar),
            out = { _, r -> r }
        )
        (negated.toBuildable() `==` 0()).commute.withAction { v, _ ->
            Rewrite.DoubleNegatedVar(v)
        }
    }

    // Matches `(Var ? 1 : 0) == 0`
    private val negated = PatternDSL.build {
        (boolToInt(Pattern.FromVar.anyVar).toBuildable() `==` 0()).commute.withAction { v, _ ->
            Rewrite.NegatedVar(v)
        }
    }

    // It's important to run doubleNegated first, since negated will match first
    // due to the three-address format
    private val matches = PatternDSL.build {
        doubleNegated.toBuildable() lor negated.toBuildable()
    }

    fun rewrite(ctp: CoreTACProgram): CoreTACProgram {
        val matcher = PatternMatcher.compilePattern(ctp.analysisCache.graph, matches)
        val rewrites = ctp.analysisCache.graph.blocks.parallelStream().mapNotNull { b ->
            b.commands.last().maybeNarrow<TACCmd.Simple.JumpiCmd>()?.takeIf {
                it.cmd.cond is TACSymbol.Var
            }
        }.mapNotNull {
            it `to?` matcher.query(it.cmd.cond as TACSymbol.Var, it.wrapped).toNullableResult()
        }

        return rewrites.patchForEach(ctp) { (jmp, rw) ->
            replaceCommand(jmp.ptr, listOf(rw.rewriteJump(jmp.cmd)))
        }.let {
            removeUnusedAssignments(
                code = it,
                expensive = false,
                isTypechecked = true,
                isErasable = {
                    // The unused assignment optimizer won't recognize all of these as being used, since
                    // said uses may be buried in wasm/soroban specific summaries
                    !it.lhs.meta.containsKey(TACMeta.SOROBAN_ENV)
                        && !it.lhs.meta.containsKey(TACMeta.EVM_MEMORY)
                }
            )
        }
    }
}
