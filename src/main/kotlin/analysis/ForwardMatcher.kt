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
import com.certora.collect.*
import datastructures.stdcollections.*
import utils.*
import vc.data.TACCmd
import vc.data.TACExpr
import vc.data.TACSymbol
import java.math.BigInteger

/**
 * Matcher for chasing use chains; i.e., the dual of the [PatternMatcher] which chases def chains.
 *
 * Unlike the [PatternMatcher], which is a universally quantified query (i.e., all definitions much match a pattern)
 * the forward matcher here is "existential", in that it finds what use sites match a pattern, but allows for
 * use sites that do not match. However, the existence of non-matches is communicated back to the caller; see [ForwardMatcher.matchOn]
 * for details.
 *
 * ## Patterns
 * Patterns are simply expressions with "holes", very similar to the [PatternMatcher.Pattern] used in the backwards
 * matcher. One important feature is that this pattern must include a distinguished "target var". This "target var"
 * is the variable whose uses we are matching. In the [ForwardMatcherDSL], this is denoted `V`. So, for example,
 * the pattern `V + 1` would match a use of some variable where 1 is added to it. `V` can appear in exactly one location
 * within a pattern, which makes the matching mechanism "directed" in some sense; once you find a use site of the target
 * variable, you know exactly what it's use should look like.
 *
 * The target variable can be arbitrarily nested within an expression, e.g., `(V & 1) == 0`. Interpreting these
 * patterns as just another kind of expression, we have the following property: for any sub-expression e within the pattern,
 * one (and only one) of the following properties is true:
 * 1. e is the target var: V
 * 2. one of e's (strict) subexpressions contains V
 * 3. V does not appear anywhere in e
 *
 * This is another way of saying there is a unique path from the top-level pattern to the occurence of V. Subexpressions
 * of the patterm who fall into category 3 above are called "siblings", in the AST of the pattern, they are siblings to
 * the expressions which lead to `V`.
 *
 * The sibling expressions in the pattern are matched against "sibling patterns": these are "expressions with holes"
 * which cannot contain V. For example, the following is a valid forward pattern: `(V & ?) == 0`, where `?` indicates "any
 * expression". In general, a sibling pattern is a concrete "immediate" (constant or variable), a "hole" (which can have
 * arbitrary matching/post-processing logic), or an aggregate expressions whose operands are sibling patterns.
 *
 * Currently, the grammar of sibling patterns and the entire pattern only uses [vc.data.TACExpr.BinExp]. This is not
 * fundamental, but was done to get the core algorithm working for the current use cases.
 *
 * ## Matches
 * This matcher finds the use sites of `v` that match some pattern. However, given the three address code form, the
 * actual full match can be spread across multiple use sites. For example, the pattern `(V & 1) == 0` should match:
 * ```
 * w = (v & 1)
 * b = w == 0
 * ```
 *
 * But what if we also have:
 * ```
 * w = (v & 1)
 * b = w == 0
 * a = w + 1
 * ```
 *
 * We still want to know about the definition at `b` while making the caller aware of the non-matching use at `a`. However
 * this requires reasoning about the transitive uses of the values resulting from the "immediate" uses
 * of v.
 *
 * To do this we use [MatchSort]. Each *immediate* use site U (a location returned by
 * [analysis.dataflow.IUseAnalysis.useSitesAfter]) in some expression `f(v)` is matched against the pattern individually
 * and we report pattern mathcing on this level. If the use at U in f(v) matches the pattern OR
 * all of the uses of `f(v)` itself match the pattern, then we associate U with [MatchSort.Complete]. If some of the uses
 * of `f(v)` do not match the pattern (but some do) we associated it with U [MatchSort.Partial].
 * If f(v) doesn't match P at all, then we associated U with null. This is reflected in the type signature of [matchOn],
 * which returns a collection of use-site nullable [MatchSort] pairs.
 */
class ForwardMatcher(val graph: TACCommandGraph) {
    /**
     * The payload for the match, using a [tac.MetaMap] style map.
     *
     * Like the [analysis.patterns.Info] class, attempting to associate an instance of [InfoKey] with a
     * conflicting value will fail the entire pattern.
     */
    @JvmInline
    value class MatchPayload(@Suppress("Treapability") val m: TreapMap<InfoKey<*>, Any> = treapMapOf()) {
        operator fun <T: Any> plus(p: Pair<InfoKey<T>, T>): MatchPayload? {
            val (k, v) = p
            return if(k !in m) {
                MatchPayload(m + p)
            } else if(m[k] != v) {
                null
            } else {
                this
            }
        }

    }

    /**
     * A sibling pattern, as described in the class documentation. Following the rust macro syntax, we will
     * denote a sibling pattern with `$e`.
     */
    sealed interface SiblingPattern {
        /**
         * Matches any subexpression. Technically redundant with [Action] below
         */
        object Top : SiblingPattern

        /**
         * The "hole", which matches an expression `e` accepted by the callback [e]. [e] takes the
         * current [MatchPayload], the expression being matched, and the location of the expression as an [LTACCmd]
         * and returns the updated [MatchPayload] on success, or null if the patch fails.
         */
        data class Action(val e: (context: LTACCmd, exp: TACExpr, payload: MatchPayload) -> MatchPayload?) : SiblingPattern

        /**
         * A composed pattern. Matches a [vc.data.TACExpr.BinExp] of type [T], whose
         * left operand matches [leftOp] and right operand matches [rightOp].
         *
         * If [commutes] is true, then expressions of type [T] are considered to commute, and if the left/right ops
         * do not match, they are reversed, and the match retried.
         *
         * After any succesful match (commuting or otherwise) if [andAlso] is non-null, the current
         * [MatchPayload] is fed into [andAlso] along with the `exp` of type [T] and the context command
         * (the [LTACCmd] which contains `exp`)
         */
        data class Composed<T: TACExpr.BinExp>(
            val klass: Class<T>,
            val leftOp: SiblingPattern,
            val rightOp: SiblingPattern,
            val commutes: Boolean,
            val andAlso: ((context: LTACCmd, exp: T, payload: MatchPayload) -> MatchPayload?)? = null
        ) : SiblingPattern

        companion object {
            /**
             * Convenience function which returns a [SiblingPattern] that matches exactly
             * expressions which are the immediate [v].
             */
            fun exactly(v: TACSymbol.Var) = Action { _, e, m ->
                if(e is TACExpr.Sym.Var && e.s == v) {
                    m
                } else {
                    null
                }
            }

            /**
             * Convenience function which returns a [SiblingPattern] that matches exactly
             * [TACExpr.Sym.Const] expressions with the value [c].
             */
            fun exactly(c: BigInteger) = Action { _, e, m ->
                if(e is TACExpr.Sym.Const && e.s.value == c) {
                    m
                } else {
                    null
                }
            }

            /**
             * Convenience function which returns a [SiblingPattern] that matches exactly
             * [TACExpr.Sym.Const] expressions with the value [c].
             */
            fun exactly(c: Int) = exactly(c.toBigInteger())
        }
    }

    /**
     * Indicates whether all (potentially transitive) uses of the variable at a use site U match
     * the pattern [Complete] or whether only some do [Partial]. If none of (potentially transitive)
     * uses of v at U do no match, we use a null [MatchSort].
     */
    sealed interface MatchSort<T> {
        data class Complete<T>(val m: Collection<T>) : MatchSort<T> {
            init {
                require(m.isNotEmpty()) {
                    "Must have at least one result"
                }
            }
        }
        data class Partial<T>(val m: Collection<T>) : MatchSort<T> {
            init {
                require(m.isNotEmpty()) {
                    "Must have at least one result"
                }
            }
        }
    }

    /**
     * The pattern representation itself. It is not expected that users will generate these
     * instances directly as the representation is somewhat counter intuitive, but instead use the
     * [ForwardMatcherDSL].
     *
     * ## Representation
     * Recall from the class documentation above that the pattern can be viewed as a superset
     * of the tac expression grammar, with holes (represented by [SiblingPattern]) and the dedicated "match var".
     *
     * The pattern is represented as a path *from* the match var to the top-level expression (i.e., the "whole pattern").
     * Thus, each intermediate node along this path corresponds to some ancestor of the match var; these ancester nodes have
     * sibling nodes as defined in the class document. Accordingly, intermediate nodes also store the [SiblingPattern] for
     * the child which does *not* contain the match var.
     *
     * Returning to our "canonical" example, we have the following representation of the `(V & 1) == 0` pattern:
     *   V --> ( & ) --> ( == )
     *           |         |
     *           *->1      *->0
     *
     * Here the "spine" represents the path from the match var to the top-level expression.
     * The offshoots (aka `*->1` and `*->0`) represent the siblings, which in this case are always immediate operands.
     * However, if we instead matched `(V & 1) == (x + 3)`
     * we would have:
     *   V --> ( & ) --> ( == )
     *           |         |
     *           *->1      *->(x + 3)
     *
     * Here `*->1` and `*->(x + 3)` are the sibling patterns.
     * Once the entire expression is matched agains the pattern, the [MatchPayload] is transformed into an instance
     * of [T] via [TopLevel] (so called because it is invoked at the "top-level" of the pattern).
     */
    sealed interface Patt<T> {
        /**
         * An "intermediate" node, although it also includes the terminal [TopLevel]. A better name
         * might be "NotMatchVar" but "Intermediate" was catchier.
         */
        sealed interface Intermediate<T> : Patt<T>

        /**
         * The distinguished "match var", which points to the [parent] in the match (either another
         * expression in [Node] or the [TopLevel])
         */
        data class Root<T>(val parent: Intermediate<T>) : Patt<T>

        /**
         * An intermediate node representing some aggregate [vc.data.TACExpr.BinExp]
         * expression of type [R] (whose runtime type representation is given by [klass]).
         *
         * [ops] indicates which child of the expression is the sibling node. So, if we have
         * [ops] is an [Operands.RightSibling], then match var is contained in the *left*
         * operand, and the right operand is the sibling node (to be matched against
         * [analysis.ForwardMatcher.Patt.Node.Operands.RightSibling.r].
         *
         * [next] is the next [Intermediate] along the "spine" of the pattern.
         */
        data class Node<R: TACExpr.BinExp, T>(
            val klass: Class<R>,
            val ops: Operands,
            val next: Intermediate<T>
        ) : Intermediate<T> {
            /**
             * Represents information about the operands, namely which child
             * operand of this expression is the sibling operand,
             * to be matched against [patt].
             */
            sealed interface Operands {
                val patt: SiblingPattern

                /**
                 * The left child is the sibling to be matched against [l];
                 * thus the right child contains the match var.
                 */
                data class LeftSibling(val l: SiblingPattern) : Operands {
                    override val patt: SiblingPattern
                        get() = l
                }

                /**
                 * The right child is the sibling to be matched against [r],
                 * thus the righ tchild contains the match var.
                 */
                data class RightSibling(val r: SiblingPattern) : Operands {
                    override val patt: SiblingPattern
                        get() = r
                }

                /**
                 * The operation commutes, and either child could be the sibling or the match var.
                 * The operands are tried in left-as-match, right-as-sibling first (where the sibling
                 * node is matched against [patt]) and if that fails, as left-as-sibling, right-as-sibling.
                 */
                data class Commutes(val other: SiblingPattern) : Operands {
                    override val patt: SiblingPattern
                        get() = other
                }
            }
        }

        /**
         * Invoked if the entire pattern matches with the given payload. The match succeeds at some
         * expression occurence in some [LTACCmd] which is given as the context. If the successfully
         * matched expression is used as the definition of some variable, that is given as defVar.
         *
         * If the top-level match should be accepted, then a non-null [T] should be returned. null represents
         * a no-match.
         */
        data class TopLevel<T>(
            val result: (payload: MatchPayload, context: LTACCmd, defVar: TACSymbol.Var?) -> T?
        ) : Intermediate<T>
    }

    /**
     * Matches uses of [v] against [patt] starting at [at]. See the class documentation for the [MatchSort] description.
     */
    fun <T: Any> matchOn(v: TACSymbol.Var, at: CmdPointer, patt: Patt.Root<T>) : Collection<Pair<CmdPointer, MatchSort<T>?>> {
        val parent = patt.parent
        /**
         * This is the explicit "match" on the [Patt.Root], we just find all uses of the variable [v], and see
         * if those uses match the pattern pointed to by [patt]'s [Patt.Root.parent]
         */
        return graph.cache.use.useSitesAfter(v, at).map {
            it to when(parent) {
                is Patt.Node<*, T> -> {
                    graph.elab(it).maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.let { lc ->
                        traverse(lc, parent, v, MatchPayload())
                    }
                }
                is Patt.TopLevel<T> -> {
                    parent.result(MatchPayload(), graph.elab(it), null)?.let(::listOf)?.let {
                        MatchSort.Complete(it)
                    }
                }
            }
        }
    }

    /**
     * The sibling match loop, matching [e] which occurs somwhere in [ctxt]
     * against [pattern] with the current payload [m]. Returns null if match fails.
     *
     * Will traverse def-chains backwards if need be in the [SiblingPattern.Composed] case.
     */
    private fun checkSibling(ctxt: LTACCmd, e: TACExpr, pattern: SiblingPattern, m: MatchPayload) : MatchPayload? {
        when(pattern) {
            is SiblingPattern.Action -> {
                return pattern.e(ctxt, e, m)
            }
            is SiblingPattern.Composed<*> -> {
                if(e is TACExpr.Sym.Var) {
                    return graph.cache.def.defSitesOf(e.s, ctxt.ptr).singleOrNull()?.let(graph::elab)?.maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.let {
                        checkSibling(it.wrapped, it.cmd.rhs, pattern, m)
                    }
                }
                if(e !is TACExpr.BinExp) {
                    return null
                }
                /*
                 * If you don't existentially bind T this way, you can't use the star projection types.
                 */
                fun <T: TACExpr.BinExp> open(openedPatt: SiblingPattern.Composed<T>) : MatchPayload? {
                    if(!openedPatt.klass.isInstance(e)) {
                        return null
                    }
                    /*
                     * Try the declared order.
                     */
                    val t1 = checkSibling(ctxt, e.o1, openedPatt.leftOp, m)?.let { r ->
                        checkSibling(ctxt, e.o2, openedPatt.rightOp, r)
                    } ?: if(!openedPatt.commutes) {
                        return null
                    } else {
                        /*
                         * If that didn't work, and the operation commutes, try the other way.
                         */
                        checkSibling(ctxt, e.o1, openedPatt.rightOp, m)?.let { r ->
                            checkSibling(ctxt, e.o2, openedPatt.leftOp, r)
                        }
                    } ?: return null
                    if(openedPatt.andAlso == null) {
                        return t1
                    }
                    return openedPatt.andAlso.invoke(ctxt, e.uncheckedAs(), t1)
                }
                return open(pattern)
            }
            SiblingPattern.Top -> return m
        }
    }

    /**
     * The core pattern match loop. [patt] is the current pattern being matched against a use of [v] at [lc]
     * with the [curr] payload. It is an invariant that [v] appears *somewhere* in the RHS of [lc]. The goal
     * of this function is to determine if this occurence matches [patt].
     *
     * Note that [v] is not necessarily the same variable which was passed into [matchOn].
     */
    private fun <T: Any> traverse(
        lc: LTACCmdView<TACCmd.Simple.AssigningCmd.AssignExpCmd>,
        patt: Patt.Node<*, T>,
        v: TACSymbol.Var,
        curr: MatchPayload
    ): MatchSort<T>? {
        val e = lc.cmd.rhs
        /**
         * This searches for the occurence of [v] within [lc] which matches [patt]. As we traverse the expression,
         * we build up a list of ancestors of the matchee, [v]. If the pattern is to match, then these are intermediate
         * nodes of the pattern, and must be matched against the parent patterns in [Patt.Node.next]. That is,
         * if we reach [e] and find it contains [v] as one of its operands, then [e] must match [patt], [e]'s parent
         * must match the [Patt.Node.next] field of [patt], e's grand parent must match that node's next and so on.
         *
         * In other words, as the recursive stack unwinds, the intermediate nodes must match the spine
         * of the pattern starting from [patt]. This stack of patterns is represented implicitly with the continuation
         * [cont].
         *
         * At recursive calls to this function, the continuation is chained: the current value of [cont] is wrapped in
         * a new continuation. Each invocation of the wrapped continuation corresponds to a "step" along the spine
         * of the pattern. If the pattern matching needs to terminate early, because of a failure or a succesful match,
         * the continuation can simply return without invoking the wrapped [cont].
         *
         * Note that the continuation chain can "run out" if the current expression in [lc] being matched
         * only partially contains this pattern. In this case, the remaining pattern is matched against
         * the use sites of the variable [lc].
         */
        fun recurse(e: TACExpr, cont: (Patt.Intermediate<T>, MatchPayload) -> MatchSort<T>?) : MatchSort<T>? {
            if(e !is TACExpr.BinExp) {
                return null
            }
            /**
             * This looks like a sub-expression which matches [patt], does it?
             *
             * Note that the failure of the match here doesn't fail the entire pattern, it could be that we need
             * to look deeper in [e]'s subexpressions. For example, if [patt] is matching `(v + 1)`, and [e] is
             * `(v + 1) + w` then the failure to match at *this level* just means we need to go deeper.
             */
            if(patt.klass.isInstance(e)) {
                when(patt.ops) {
                    /**
                     * Either of these operands could be [v]. check left to right
                     */
                    is Patt.Node.Operands.Commutes -> {
                        if(e.o1AsNullableTACSymbol() == v) {
                            /**
                             * If the left (aka o1) operand matches, then try to unwind the stack via [cont].
                             *
                             * Note that we pass [Patt.Node.next] into [cont]: this represents that if the
                             * overall pattern is to match, then the parent of [e] (this caller) must match the
                             * parent pattern of [patt].
                             */
                            checkSibling(lc.wrapped, e = e.o2, m = curr, pattern = patt.ops.other)?.let {
                                cont(patt.next, it)
                            }?.let { return it }
                        }
                        /**
                         * Ibid, mm.
                         */
                        if(e.o2AsNullableTACSymbol() == v) {
                            checkSibling(lc.wrapped, e = e.o1, m = curr, pattern = patt.ops.other)?.let {
                                cont(patt.next, it)
                            }?.let { return it }
                        }
                    }
                    /**
                     * Very similar to the above cases, but we know which operand to check against [v]
                     */
                    is Patt.Node.Operands.LeftSibling -> {
                        /**
                         * Aren't you getting this backwards? No, [analysis.ForwardMatcher.Patt.Node.Operands.LeftSibling]
                         * means that the *left* operand is the sibling, so the *right* operand is the matchee (aka [v])
                         */
                        if(e.o2AsNullableTACSymbol() == v) {
                            checkSibling(lc.wrapped, e = e.o2, m = curr, pattern = patt.ops.l)?.let { r ->
                                cont(patt.next, r)
                            }?.let { return it }
                        }
                    }
                    is Patt.Node.Operands.RightSibling -> {
                        /**
                         * Ibid, the right operand is the sibling, so check the left operand for [v].
                         */
                        if(e.o1AsNullableTACSymbol() == v) {
                            checkSibling(lc.wrapped, e = e.o2, m = curr, pattern = patt.ops.r)?.let { r ->
                                cont(patt.next, r)
                            }?.let {
                                return it
                            }
                        }
                    }
                }
            }
            /**
             * Immediate match didn't work. Look for [patt] in the operands of [e].
             *
             * Let's look carefully at what this continuation is doing. By creating a new closure, we effectively
             * record [e], and try to find a match in our left operand. If the continuation we create here
             * is called, it means that we found a match in our left child, nested arbitrarily deep. As the continuation
             * stack is unwound, which corresponds both to a "step" along the spine of the pattern, and traveling
             * back "up" the expression AST, we eventually reach this continuation. It is called with some [Patt.Intermediate]
             * which is what [e] must match for the overall match to succeed. This pattern can have two forms,
             * a [Patt.TopLevel] or [Patt.Intermediate]. If [Patt.TopLevel], then if the [Patt.TopLevel.result] callback
             * accepts the current payload, we stop unwinding the continuation stack.
             *
             * Otherwise, we see if the [Patt.Node] expects the sibling to be in the *right* child. Why the right?
             * Well, because we *initially* recursed into [vc.data.TACExpr.BinExp.o1] and are now bubbling up, that means the
             * match var occurred within the left child, and thus the right child is the sibling. If that sibling check passes,
             * then [e] matches [Patt.Node], and [e]'s parent needs to match its [Patt.Node.next], which we do by
             * calling the continuation. These steps are annotated below.
             *
             * For example, suppose we are matching `(V + 1) + w` which means [Patt] is `(V + 1)` with
             * it's `next` field pointing to a pattern `[] + w`, where `[]` represents "the subexpression that matches".
             * Suppose that [e] is exactly the expression `(v + 1) + w`.
             * When we recurse on the left operand of [e] (which is `(v + 1)`) we get a match, and start bubbling up. We thus
             * call this continuation with nxt = `[] + w`, meaning we need to check the *right* operand of [e] against `w`
             */
            val r1 = recurse(e.o1) rec@{ nxt, m ->
                /**
                 * We are bubbling up with a successful match found in our left child, which requires this expression [e]
                 * matches [nxt].
                 */
                when(nxt) {
                    /**
                     * Then [e] needs to match `[] <op> $e` or `$e <op> []` where `[]` is "the subexpression that matched"
                     * (aka [vc.data.TACExpr.BinExp.o1]) and $e is the sibling (aka the right child [vc.data.TACExpr.BinExp.o2])
                     */
                    is Patt.Node<*, T> -> {
                        /**
                         * Well, we have the wrong kind of `op`. Fail the pattern.
                         */
                        if(!nxt.klass.isInstance(e)) {
                            return@rec null
                        }
                        when(nxt.ops) {
                            /**
                             * Because we're bubbling up from the left, we know that the sibling has to be the right child
                             * (as denoted by [analysis.ForwardMatcher.Patt.Node.Operands.RightSibling]) OR the op
                             * has to be commutative [analysis.ForwardMatcher.Patt.Node.Operands.Commutes].
                             *
                             */
                            is Patt.Node.Operands.RightSibling,
                            is Patt.Node.Operands.Commutes -> {
                                /**
                                 * check that the sibling node matches
                                 */
                                checkSibling(lc.wrapped, pattern = nxt.ops.patt, m = m, e = e.o2)?.let {
                                    /**
                                     * If it does, then take the parent pattern of [nxt], and insist that our
                                     * parent must match it as well.
                                     */
                                    cont(nxt.next, it)
                                }
                            }
                            /**
                             * Wrong side, no match
                             */
                            is Patt.Node.Operands.LeftSibling -> null
                        }
                    }
                    is Patt.TopLevel -> {
                        /**
                         * Actually, o1 was the complete match, so let's do the top level test here, and stop
                         * bubbling
                         */
                        nxt.result.invoke(m, lc.wrapped, null)?.let(::listOf)?.let { MatchSort.Complete(it) }
                    }
                }
            }
            /**
             * We found a match in our left child, greedily take that result
             */
            if(r1 != null) {
                return r1
            }
            /**
             * Otherwise try in our right child. The continuation is the "dual" of the above one, but with right and
             * left swapped.
             */
            val r2 = recurse(e.o2) rec@{ nxt, m ->
                when(nxt) {
                    is Patt.Node<*, T> -> {
                        if(nxt.klass.isInstance(e)) {
                            return@rec null
                        }
                        when(nxt.ops) {
                            is Patt.Node.Operands.Commutes,
                            is Patt.Node.Operands.LeftSibling -> {
                                checkSibling(lc.wrapped, pattern = nxt.ops.patt, m = m, e = e.o1)?.let {
                                    cont(nxt.next, it)
                                }
                            }
                            is Patt.Node.Operands.RightSibling -> {
                                null
                            }
                        }
                    }
                    is Patt.TopLevel -> {
                        nxt.result.invoke(m, lc.wrapped, null)?.let(::listOf)?.let { MatchSort.Complete(it) }
                    }
                }
            }
            return r2
        }
        /**
         * Now we are done with how the recursion loop works, let's see how it is used. We start search for [v] in
         * [lc] which matches [patt]. The continuation here handles the case where the bubbling goes exhausts the current
         * expression. Then there are two cases to consider. The first is if the next pattern to check is a [Patt.TopLevel];
         * in this case, we can simply run the [Patt.TopLevel.result] ourself, letting it know via the defVar parameter
         * that the matching use was at a definition for [lc]'s [vc.data.TACCmd.Simple.AssigningCmd.AssignExpCmd.lhs].
         *
         * In the other case, it means we have:
         * `w = rhs`
         * and we found a match on [v]  with some payload `m` in `rhs`, but we have some residual pattern `[] <op> $e` or `$e <op> []`, that is,
         * "rhs" is the "subexpression that matched" (`[]`) but we need to see more uses to declare a complete match.
         * In this case, we simply recursively invoke [traverse], setting [lc] = use site of w, [v] = w, and [patt] = `[] <op> $e`,
         * and [curr] = `m`.
         */
        return recurse(e) { nxt, m ->
            when(nxt) {
                is Patt.Node<*, T> -> {
                    /**
                     * Find all use sites of this command's lhs, and see if they match the residual pattern in [nxt].
                     * If some do, use [MatchSort.Partial]; if all do, use [MatchSort.Complete]; if none do, declare
                     * a match failure and return null.
                     */
                    graph.cache.use.useSitesAfter(lc.cmd.lhs, lc.ptr).fold(listOf<T>() to true) { (acc, isComplete), nxtUse ->
                        val res = graph.elab(nxtUse).maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.let {
                            traverse(
                                it, nxt, lc.cmd.lhs, m
                            )
                        }
                        when(res) {
                            is MatchSort.Complete -> {
                                (acc + res.m) to isComplete
                            }
                            is MatchSort.Partial -> {
                                (acc + res.m) to false
                            }
                            null -> acc to false
                        }
                    }.takeIf { (acc, _) ->
                        acc.isNotEmpty()
                    }?.let { (acc, isComplete) ->
                        if(isComplete) {
                            MatchSort.Complete(acc)
                        } else {
                            MatchSort.Partial(acc)
                        }
                    }
                }
                /**
                 * This is a complete match of the pattern
                 */
                is Patt.TopLevel -> {
                    nxt.result.invoke(m, lc.wrapped, lc.cmd.lhs)?.let(::listOf)?.let { MatchSort.Complete(it) }
                }
            }
        }
    }
}
