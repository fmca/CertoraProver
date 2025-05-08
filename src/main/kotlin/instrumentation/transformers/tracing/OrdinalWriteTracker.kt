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

import analysis.CommandWithRequiredDecls
import datastructures.stdcollections.*
import instrumentation.transformers.tracing.BufferTraceInstrumentation.Companion.`=`
import instrumentation.transformers.tracing.BufferTraceInstrumentation.Companion.flatten
import vc.data.*
import vc.data.TACProgramCombiners.andThen

internal data class OrdinalWriteTracker(
    val writeCount: TACSymbol.Var,
    val writeVars: Map<Int, TACSymbol.Var>
) : InstrumentationMixin {
    override fun atPrecedingUpdate(
        s: IBufferUpdate,
        overlapSym: TACSymbol.Var,
        writeEndPoint: TACSymbol.Var,
        baseInstrumentation: ILongReadInstrumentation
    ): CommandWithRequiredDecls<TACCmd.Simple> {
        val valueUpdate = when(val src = s.updateSource) {
            is IWriteSource.ByteStore -> {
                writeVars.map { (ind, v) ->
                    v `=` {
                        ite(
                            overlapSym and (ind.asTACExpr eq writeCount),
                            src.writeSymbol,
                            v
                        )
                    }
                }.flatten()
            }
            else -> CommandWithRequiredDecls<TACCmd.Simple>()
        }
        return valueUpdate andThen (writeCount `=` {
            ite(overlapSym, writeCount add TACSymbol.One, writeCount)
        })
    }

    override fun atLongRead(s: ILongRead): CommandWithRequiredDecls<TACCmd.Simple> {
        return CommandWithRequiredDecls()
    }

    override val havocInitVars: List<TACSymbol.Var>
        get() = writeVars.values.toList()

    override val constantInitVars: List<Pair<TACSymbol.Var, ToTACExpr>>
        get() = listOf(writeCount to TACExpr.zeroExpr)

}
