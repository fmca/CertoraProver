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

package analysis

import analysis.patterns.InfoKey
import vc.data.TACExpr
import vc.data.TACSymbol
import java.math.BigInteger

/**
 * DSL Builder for the [ForwardMatcher]. Abstracts over having to build [ForwardMatcher.Patt] instances yourself.
 */
object ForwardMatcherDSL {
    enum class OperandOrder {
        SIBLING_LEFT,
        SIBLING_RIGHT,
        COMMUTE
    }

    /**
     * The "AST representation" of the pattern, where the variable to be matched [PatternNode.Root] is nested
     * in some sub-expression. Once the pattern building is complete, this AST is "inverted" to give the "child to root"
     * representation used by [ForwardMatcher.Patt]
     */
    sealed interface PatternNode {
        /**
         * Corresponds to an intermediate [ForwardMatcher.Patt.Node] node. The operand order [OperandOrder] says
         * whether the [sibling] is the left or right child compared to the "spine" of the match in [child].
         * [klass] is the expected type of the [TACExpr.BinExp] to match against.
         */
        data class Intermediate<R: TACExpr.BinExp>(
            val child: PatternNode,
            val sibling: ForwardMatcher.SiblingPattern,
            val mode: OperandOrder,
            val klass: Class<R>
        ) : PatternNode

        /**
         * The "match var".
         */
        data object Root : PatternNode
    }

    /**
     * Predicates against arbitrary variables.
     */
    fun v(f: (LTACCmd, TACSymbol.Var, ForwardMatcher.MatchPayload) -> ForwardMatcher.MatchPayload?) = ForwardMatcher.SiblingPattern.Action { l, e, m ->
        if(e is TACExpr.Sym.Var) {
            f(l, e.s, m)
        } else {
            null
        }
    }

    /**
     * Matches any constant and associates it with [nm] in the current payload. NB that if [nm] is
     * bound to a different value this will fail the match.
     */
    fun k(nm: InfoKey<BigInteger>) = ForwardMatcher.SiblingPattern.Action { _, e, m ->
        if(e is TACExpr.Sym.Const) {
            m + (nm to e.s.value)
        } else {
            null
        }
    }

    /**
     * Matches any variable and associates it with [nm] in the current payload. NB that if [nm] is
     * bound to a different variable, this will fail the match.
     */
    fun v(nm: InfoKey<TACSymbol.Var>) = ForwardMatcher.SiblingPattern.Action { _, e, m ->
        if(e is TACExpr.Sym.Var) {
            m + (nm to e.s)
        } else {
            null
        }
    }

    /**
     * Intermediate class returned by the DSL, to be turned into a [ForwardMatcher.Patt] via [withAction] (which
     * constructs the [ForwardMatcher.Patt.TopLevel].
     */
    class ExpectAction(val n: PatternNode) {
        /**
         * Turns the partial DSL result into a [ForwardMatcher.Patt], where the returned [ForwardMatcher.Patt] uses
         * [ForwardMatcher.Patt.TopLevel] whose [analysis.ForwardMatcher.Patt.TopLevel.result] field is just [f].
         */
        fun <T> withAction(f: (m: ForwardMatcher.MatchPayload, l: LTACCmd, v: TACSymbol.Var?) -> T?): ForwardMatcher.Patt.Root<T> {
            /**
             * Inverts the AST view in [PatternNode] and produces the [ForwardMatcher.Patt.Root] version.
             */
            tailrec fun inversionLoop(l: PatternNode, curr: ForwardMatcher.Patt.Intermediate<T>) : ForwardMatcher.Patt.Root<T> {
                when(l) {
                    is PatternNode.Intermediate<*> -> {
                        fun <R: TACExpr.BinExp> openInter(i: PatternNode.Intermediate<R>) : ForwardMatcher.Patt.Intermediate<T> {
                            val ops = when(i.mode) {
                                OperandOrder.SIBLING_LEFT -> {
                                    ForwardMatcher.Patt.Node.Operands.LeftSibling(
                                        l = i.sibling
                                    )
                                }
                                OperandOrder.SIBLING_RIGHT -> {
                                    ForwardMatcher.Patt.Node.Operands.RightSibling(
                                        r = i.sibling
                                    )
                                }
                                OperandOrder.COMMUTE -> {
                                    ForwardMatcher.Patt.Node.Operands.Commutes(i.sibling)
                                }
                            }
                            return ForwardMatcher.Patt.Node(
                                klass = i.klass,
                                next = curr,
                                ops = ops
                            )
                        }
                        return inversionLoop(l.child, openInter(l))
                    }
                    PatternNode.Root -> {
                        return ForwardMatcher.Patt.Root(
                            parent = curr
                        )
                    }
                }
            }
            /**
             * Start the inversion with the [ForwardMatcher.Patt.TopLevel] that uses [f].
             */
            return inversionLoop(n, ForwardMatcher.Patt.TopLevel(f))
        }
    }

    val V = PatternNode.Root

    fun build(f: context(ForwardMatcherDSL, ForwardDSLBuilder)() -> PatternNode) : ExpectAction {
        return ExpectAction(f(this, ForwardDSLBuilder))
    }
}
