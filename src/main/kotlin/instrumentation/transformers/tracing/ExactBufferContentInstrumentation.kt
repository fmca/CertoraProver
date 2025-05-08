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
package instrumentation.transformers.tracing

import datastructures.stdcollections.*
import analysis.CommandWithRequiredDecls
import evm.EVM_WORD_SIZE
import evm.MASK_SIZE
import tac.Tag
import vc.data.*
import vc.data.TACProgramCombiners.andThen

/**
 * Intentionally undocumented, as this is a performance nightmare
 * and will probably be deleted.
 *
 * In brief: tries to construct a precise model of memory using chained bytemap
 * definitions. It "works", but makes the solver *very* sad
 */
internal data class ExactBufferContentInstrumentation(
    val preciseContentsMap: TACSymbol.Var
) : InstrumentationMixin {
    override fun atPrecedingUpdate(
        s: IBufferUpdate,
        overlapSym: TACSymbol.Var,
        writeEndPoint: TACSymbol.Var,
        baseInstrumentation: ILongReadInstrumentation
    ): CommandWithRequiredDecls<TACCmd.Simple> {
        val prevMap = TACKeyword.TMP(Tag.ByteMap, "!prev")

        val relativeStart = TACKeyword.TMP(Tag.Int, "!relStart")

        val idx = TACKeyword.TMP(Tag.Bit256, "!idx")

        val baseCase = TACExpr.Select(prevMap.asSym(), idx.asSym(), Tag.Bit256)

        val (extra, newDef) = when(val src = s.updateSource) {
            is IWriteSource.ByteStore -> {
                val writtenVal = TACKeyword.TMP(Tag.Bit256, "!writtenVal")
                CommandWithRequiredDecls(
                    listOf(
                        TACCmd.Simple.AssigningCmd.AssignExpCmd(
                            lhs = writtenVal,
                            rhs = src.writeSymbol
                        )
                    ), setOf(writtenVal, src.writeSymbol)
                ) to generateIteTree(baseCase, idxParam = idx, writtenVal = writtenVal, relativeOffset = relativeStart)
            }
            is IWriteSource.EnvCopy,
            is IWriteSource.LongMemCopy,
            is IWriteSource.Other -> {
                CommandWithRequiredDecls<TACCmd.Simple>() to with(TACExprFactTypeCheckedOnlyPrimitives) {
                    ite(
                        (relativeStart le idx) and
                            (idx lt (relativeStart intAdd s.updateLoc)),
                        TACExpr.Unconstrained(Tag.Bit256),
                        baseCase
                    )
                }
            }
        }
        val newMapDef = TACKeyword.TMP(Tag.ByteMap, "!newDef")
        return extra andThen CommandWithRequiredDecls(
            listOf(
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = relativeStart,
                    rhs = TACExpr.BinOp.IntSub(
                        s.updateLoc.asSym(), baseInstrumentation.baseProphecy.asSym()
                    )
                ),
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = prevMap,
                    rhs = preciseContentsMap,
                ),
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = newMapDef,
                    rhs = TACExpr.MapDefinition(listOf(idx.asSym()), newDef, Tag.ByteMap)
                ),
                TACCmd.Simple.AssigningCmd.AssignExpCmd(
                    lhs = preciseContentsMap,
                    rhs = TACExpr.TernaryExp.Ite(
                        i = overlapSym.asSym(),
                        t = newMapDef.asSym(),
                        e = prevMap.asSym()
                    )
                )
            ),
            setOf(
                preciseContentsMap,
                prevMap,
                relativeStart,
                overlapSym,
                baseInstrumentation.baseProphecy,
                newMapDef
            )
        )
    }

    context(TACExprFact)
    private fun TACSymbol.Var.byteAt(msbIndex: Int) = (this shiftRLog ((31 - msbIndex) * 8).asTACExpr) bwAnd MASK_SIZE(8).asTACExpr


    private fun generateIteTree(
        idxParam: TACSymbol.Var,
        relativeOffset: TACSymbol.Var,
        writtenVal: TACSymbol.Var,
        base: Int,
        sz: Int
    ) : TACExpr = TACExprFactTypeCheckedOnlyPrimitives {
        require(sz % 2 == 0)
        val midPoint = sz / 2
        val (beforeMidBranch, afterMidBranch) = if (sz < 8) {
            val finalLowerInd = base + midPoint - 1
            val lowerBaseCase = writtenVal.byteAt(finalLowerInd)
            val finalUpperInd = base + sz - 1
            val upperBaseCase = writtenVal.byteAt(finalUpperInd)
            generateIteChain(
                baseCase = lowerBaseCase,
                ind = base,
                stop = finalLowerInd,
                idxParam,
                writtenVal,
                relativeOffset
            ) to
                    generateIteChain(
                        baseCase = upperBaseCase,
                        ind = base + midPoint,
                        stop = finalUpperInd,
                        idxParam,
                        writtenVal,
                        relativeOffset
                    )
        } else {
            generateIteTree(
                idxParam,
                relativeOffset, writtenVal, base, sz / 2
            ) to generateIteTree(
                idxParam,
                relativeOffset, writtenVal, base + (sz / 2), sz / 2
            )
        }
        ite(
            idxParam lt (relativeOffset intAdd (base + midPoint).asIntTACExpr),
            beforeMidBranch,
            afterMidBranch
        )
    }

    private fun generateIteTree(
        baseCase: TACExpr,
        relativeOffset: TACSymbol.Var,
        writtenVal: TACSymbol.Var,
        idxParam: TACSymbol.Var,
    ) : TACExpr = TACExprFactTypeCheckedOnlyPrimitives {
        ite(
            not(
                (relativeOffset le idxParam) and (idxParam lt (relativeOffset intAdd EVM_WORD_SIZE.asIntTACExpr))
            ),
            baseCase,
            generateIteTree(idxParam, relativeOffset, writtenVal, 0, 32)
        )
    }

    private fun generateIteChain(
        baseCase: TACExpr,
        ind: Int,
        stop: Int,
        idxParam: TACSymbol.Var,
        writtenVal: TACSymbol.Var,
        relativeOffset: TACSymbol.Var
    ) : TACExpr = with(TACExprFactTypeCheckedOnlyPrimitives) {
        if(ind == stop) {
            baseCase
        } else {
            ite(
                idxParam eq (ind.asIntTACExpr intAdd relativeOffset.asSym()),
                writtenVal.byteAt(ind),
                generateIteChain(baseCase, ind + 1, stop, idxParam, writtenVal, relativeOffset)
            )
        }
    }

    override fun atLongRead(s: ILongRead): CommandWithRequiredDecls<TACCmd.Simple> {
        return CommandWithRequiredDecls()
    }

    private val dummyIdx = TACKeyword.TMP(Tag.Bit256, "!idx")

    override val havocInitVars: List<TACSymbol.Var>
        get() = listOf()
    override val constantInitVars: List<Pair<TACSymbol.Var, ToTACExpr>>
        get() = listOf(
            preciseContentsMap to TACExpr.MapDefinition(
                listOf(
                    dummyIdx.asSym()
                ), TACExpr.zeroExpr, Tag.ByteMap
            )
        )

}
