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

package analysis.opt

import analysis.*
import evm.MAX_EVM_UINT256
import utils.*
import vc.data.*
import datastructures.stdcollections.*

/**
 * Tries to find cases where the value written into the free pointer is
 * reused later, and replaces these cases with a fresh read if necessary.
 * For example, we have seen:
 * ```
 * tacM0x40 = v
 * ...
 * mem[v] = len
 * ```
 * when allocating a new array after the previous allocation. Reusing the free pointer
 * like this is *very* confusing for the alloc analysis.
 *
 * Thus, we rewrite the above to:
 * ```
 * tacM0x40 = v
 * freshRead = tacM0x40
 *
 * mem[freshRead] = len
 * ```
 * However, if there is another alias "in scope" at the use site, we just use that:
 * ```
 * tacM0x40 = v
 * // no writes to tacM0x40...
 * w = tacMx040
 * mem[v] = len
 * ```
 * will be rewritten to:
 * ```
 * tacM0x40 = v
 * w = tacM0x40
 * mem[w] = len
 * ```
 */
object FreePointerReadFixer : FreePointerReadFixupMixin<FreePointerReadFixer.FPUpdate> {

    private data class FPUpdate(
        override val fpAlias: TACSymbol.Var,
        override val rewriteUseAfter: CmdPointer
    ) : FreePointerReadFixupMixin.ReplacementCandidate
    /*
      Find cases where the RHS written as the new value of the free pointer is reused instead
      of reading the FP fresh, replace those with a fresh read.
     */
    fun fixFreePointerRead(p: CoreTACProgram) : CoreTACProgram {
        val live = p.analysisCache.lva
        return p.parallelLtacStream().filter {
            it.cmd is TACCmd.Simple.AssigningCmd.AssignExpCmd && it.cmd.lhs == TACKeyword.MEM64.toVar() &&
                    it.cmd.rhs is TACExpr.Sym.Var
        }.map {
            it.enarrow<TACExpr.Sym.Var>()
        }.filter {
            // find those writes whose RHS is still live
            it.exp.s in live.liveVariablesAfter(it.ptr)
        }.map {
            FPUpdate(
                it.exp.s, it.ptr
            )
        }.doRewrite(p)
    }

    private val penultimateLengthWrite = PatternDSL.build {
        ((Var - !TACKeyword.MEM64.toVar()).locFirst - 32()).first
    }

    /*
     * Find a missing free pointer write!
     */
    fun addMissingFreePointerWrite(c: CoreTACProgram) : CoreTACProgram {
        val comp = PatternMatcher.compilePattern(
                patt = penultimateLengthWrite,
                graph = c.analysisCache.graph
        )
        return c.patching {
            c.parallelLtacStream().filter {
                it.cmd is TACCmd.Simple.AssigningCmd.ByteStore && it.cmd.value is TACSymbol.Var
            }.map {
                it.narrow<TACCmd.Simple.AssigningCmd.ByteStore>()
            }.mapNotNull {
                it `to?` comp.query(it.cmd.value as TACSymbol.Var, it.wrapped).toNullableResult()
            }.filter { (storeLoc, res) ->
                val subtractOp = (res.first.enarrow<TACExpr.BinOp.Sub>().exp.o2 as? TACExpr.Sym.Var ?: return@filter false).s
                val loc = storeLoc.cmd.loc as? TACSymbol.Var ?: return@filter false
                if(res.first.ptr.block != storeLoc.ptr.block) {
                    return@filter false
                }
                /*
                   What we're subtracting has to be where we're writing as well
                 */
                if(subtractOp !in c.analysisCache.gvn.findCopiesAt(target = res.first.ptr, source = storeLoc.ptr to loc)) {
                    return@filter false
                }
                val d = c.analysisCache.use.useSitesAfter(res.second, res.first.ptr).takeIf {
                    it.isNotEmpty()
                }?.let { d ->
                    d.singleOrNull()?.let(c.analysisCache.graph::elab)?.maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.takeIf {
                            val rhs = it.cmd.rhs
                            rhs is TACExpr.Vec.Add && rhs.operandsAreSyms() &&
                                    rhs.ls.any {
                                        it == res.second.asSym()
                                    } && rhs.ls.any {
                                it == 0x1f.toBigInteger().asTACSymbol().asSym()
                            }
                    }?.let {
                        c.analysisCache.use.useSitesAfter(it.cmd.lhs, it.ptr).singleOrNull()
                    }?.let(c.analysisCache.graph::elab)?.maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.takeIf andCheck@{
                        val rhs = it.cmd.rhs
                        if(rhs !is TACExpr.BinOp.BWAnd) {
                            return@andCheck false
                        }
                        val lowerMask = MAX_EVM_UINT256.andNot(0x1f.toBigInteger()).asTACSymbol().asSym()
                        rhs.o1 is TACExpr.Sym && rhs.o2 is TACExpr.Sym && (rhs.o1 == lowerMask || rhs.o2 == lowerMask)
                    }?.let {
                        c.analysisCache.use.useSitesAfter(it.cmd.lhs, it.ptr)
                    } ?: d
                } ?: return@filter false
                d.none {
                    c.analysisCache.graph.elab(it).maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.let {
                        it.cmd.lhs == TACKeyword.MEM64.toVar() && it.cmd.rhs is TACExpr.Sym.Var
                    } == true
                }
            }.map {
                it.first.ptr to TACCmd.Simple.AssigningCmd.AssignExpCmd(
                        lhs = TACKeyword.MEM64.toVar(),
                        rhs = it.second.second.asSym()
                )
            }.sequential().forEach {(where, toAppend) ->
                it.replace(where) { cmd ->
                    listOf(cmd, toAppend)
                }
            }
        }
    }
}
