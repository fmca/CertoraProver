/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY, without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR a PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
package verifier.equivalence

import analysis.CmdPointer
import analysis.TACCommandGraph
import datastructures.stdcollections.*
import log.*
import solver.CounterexampleModel
import utils.*
import vc.data.TACCmd
import vc.data.TACExpr
import vc.data.TACSymbol
import verifier.equivalence.CEXUtils.asEither
import java.math.BigInteger

private val logger = Logger(LoggerTypes.EQUIVALENCE)

/**
 * Generic class for "chasing" bytemap definitions in a counter example. The chase is determined by the [Visitor]
 * interface, see below.
 */
object BufferExtraction {
    /**
     * The result of a visit operation of [Visitor].
     */
    sealed interface VisitResult<out T> {
        /**
         * Halt the def chasing and yield the result [r].
         */
        data class Done<T>(val r: T) : VisitResult<T>

        /**
         * Continue chasing the definition of the bytemap after this current step (longstore or store).
         * The continuation [cont] is used to elaborate the result of this further chasing: if the result
         * of chasing is some value `Either.Left(t)`, then `t` is passed to [cont] and this is yielded
         * as the result of this step.
         *
         * Could be called bind.
         */
        data class Continue<T>(val cont: (T) -> Either<T, String>): VisitResult<T>

        /**
         * Indicates that the visiting should halt with an error.
         */
        data class Err(val s: String) : VisitResult<Nothing>
    }

    /**
     * Called on each "step" of the bytemap definition found in the program.
     * The final value of the bytemap is determined by a sequence of store / longstores,
     * bottoming out at some map definition. The chain of definitions for a bytemap are chased backwards;
     * each store/longstore/map def encountered corresponding to a call on this interface. NB that the
     * functions here are called in reverse program order.
     */
    interface Visitor<T> {
        /**
         * Called when the definition of the current bytemap is given by a store operation at [where].
         * The index being written to is [idxValue]; the value being written was [writtenExpr] which evaluates to [writtenValue]
         * in the counter example model.
         *
         * If this step returns [VisitResult.Continue], then the definition of the bytemap that is the target
         * of the the store operation will be visited.
         */
        fun onStore(
            where: CmdPointer,
            idxValue: BigInteger,
            writtenValue: BigInteger,
            writtenExpr: TACExpr
        ) : VisitResult<T>

        /**
         * Called when the definition of the current bytemap is a longstore operation at [where]. The output offset in
         * the bytemap is [targetLocation], at which [length] bytes are copied. The source of the longcopy is the variable [sourceMap] (if known)
         * and the source offset (if known) is [sourceOffset].
         *
         * If this visitor returns [VisitResult.Continue], then the definition of the bytemap into which the longstore is performed
         * will be visited.
         */
        fun onLongCopy(
            where: CmdPointer,
            targetLocation: BigInteger,
            length: BigInteger,
            sourceMap: TACSymbol.Var?,
            sourceOffset: BigInteger?
        ) : VisitResult<T>

        /**
         * Called when the definition of the current bytemap is a [TACExpr.MapDefinition] expression at [where].
         * There is no possibility of continuation at this point this is the "base case" for the visiting process.
         * Thus, this visit step is expected to return [T] or String, indicating a successful result or error respectively.
         * If [T] is returned, then this value is bubbled up through any [VisitResult.Continue.cont] on the "stack".
         */
        fun onMapDefinition(where: CmdPointer) : Either<T, String>
    }

    /**
     * "Extract" information from a buffer variable [bufferVar] at [where] in [graph] using some counterexample [model].
     * [visitor] determines how the steps that define [bufferVar] are translated into some result of type [T].
     * If the extraction fails, either due to an explicit error raised by [visitor] or in the extraction process,
     * a descriptive error message is returned via the [Either.Right] variant.
     */
    fun <T> extractBuffer(
        graph: TACCommandGraph,
        model: CounterexampleModel,
        bufferVar: TACSymbol.Var,
        where: CmdPointer,
        visitor: Visitor<T>
    ) : Either<T, String> {
        return Interpreter(visitor = visitor, graph = graph, model = model).extractMap(v = bufferVar, where = where)
    }

    /**
     * Internal class to do the extraction looping. [visitor], [graph], and [model] are all "context" variables that
     * are global to the looping process, and are thus state variables.
     */
    private class Interpreter<T>(
        val visitor: Visitor<T>,
        val model: CounterexampleModel,
        val graph: TACCommandGraph
    ) {
        /**
         * Trace the definition of the bytemap [v] at [where].
         */
        fun extractMap(
            v: TACSymbol.Var,
            where: CmdPointer
        ) : Either<T, String> {
            logger.trace {
                "Tracing definition of $v from $where"
            }
            // no need to filter by reachable blocks, maps are in SSA so there is actually only one assignment
            val def = graph.cache.def.defSitesOf(v, where).singleOrNull()?.let(graph::elab) ?: return "No single def site for $v at $where".toRight()
            if(def.cmd !is TACCmd.Simple.AssigningCmd.AssignExpCmd) {
                return "Unrecognized definition format at $def for $v at @ $where".toRight()
            }
            /**
             * Mutual recursion between the expression interpretation and the result handling. Done with late initialization
             * to "close the loop".
             */
            lateinit var resHandler: (TACExpr, VisitResult<T>) -> Either<T, String>

            /**
             * Descend into an (arbitrarily) nested expression defining a bytemap. If the expression format in [e]
             * is not something we expect for a bytemap, this returns an error.
             */
            fun interpretLoop(
                e: TACExpr
            ) : Either<T, String> {
                return when(e) {
                    is TACExpr.TernaryExp.Ite -> {
                        val cond = (e.i as? TACExpr.Sym)?.s ?: return "ite does not have expression we understand ${e.i} @ $def".toRight()
                        model.valueAsBoolean(cond).mapRight { "Couldn't interpret ite $e @ $def" }.bindLeft { flg ->
                            logger.trace {
                                "Interpreted flag in $e as $flg"
                            }
                            if(flg) {
                                interpretLoop(e.t)
                            } else {
                                interpretLoop(e.e)
                            }
                        }
                    }
                    is TACExpr.Store -> {
                        val ind = model.evalExprByRhs(e.loc).asEither { "Couldn't get index from $e @ $def" }.leftOr { return it }
                        val value = model.evalExprByRhs(e.value).asEither { "Couldn't get value from $e @ $def" }.leftOr { return it }
                        return resHandler(e.base, visitor.onStore(
                            where = where,
                            idxValue = ind,
                            writtenValue = value,
                            writtenExpr = e.value
                        ))

                    }
                    is TACExpr.LongStore -> {
                        val targetInd = model.evalExprByRhs(e.dstOffset).asEither { "Couldn't get target index from $e @ $def" }.leftOr { return it }
                        val sourceMap = (e.srcMap as? TACExpr.Sym.Var)?.s
                        val sourceOffset = model.evalExprByRhs(e.srcOffset).takeIf { it.first }?.second
                        val len = model.evalExprByRhs(e.length).asEither { "Couldn't get length from $e @ $def" }.leftOr { return it }
                        return resHandler(e.dstMap, visitor.onLongCopy(
                            where = where,
                            length = len,
                            sourceOffset = sourceOffset,
                            sourceMap = sourceMap,
                            targetLocation = targetInd
                        ))
                    }
                    is TACExpr.Sym.Var -> {
                        /**
                         * Go to the outer loop, we need to go chase this variable definition
                         */
                        extractMap(e.s, def.ptr)
                    }
                    is TACExpr.MapDefinition -> {
                        visitor.onMapDefinition(where)
                    }
                    else -> "Hit unrecognized expression $e at $def".toRight()
                }
            }
            /**
             * Function for handling the result of visiting a bytemap definition, and recursing into `e` (the "target" of the
             * visited operation) if visit is returned.
             */
            resHandler = { e, res: VisitResult<T> ->
                when(res) {
                    is VisitResult.Continue -> {
                        interpretLoop(e).bindLeft {
                            res.cont(it)
                        }
                    }
                    is VisitResult.Done -> res.r.toLeft()
                    is VisitResult.Err -> res.s.toRight()
                }
            }
            return interpretLoop(def.cmd.rhs)
        }
    }

}
