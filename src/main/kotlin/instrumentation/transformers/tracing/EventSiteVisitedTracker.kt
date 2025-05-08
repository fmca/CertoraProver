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
import vc.data.TACCmd
import vc.data.TACSymbol
import vc.data.ToTACExpr
import datastructures.stdcollections.*

/**
 * Extremelye simple instrumentation, if the long read is hit, set [siteVisited] to true.
 *
 * Does what it says on the tin.
 */
internal data class EventSiteVisitedTracker(
    val siteVisited: TACSymbol.Var
) : InstrumentationMixin {
    override fun atPrecedingUpdate(
        s: IBufferUpdate,
        overlapSym: TACSymbol.Var,
        writeEndPoint: TACSymbol.Var,
        baseInstrumentation: ILongReadInstrumentation
    ): CommandWithRequiredDecls<TACCmd.Simple> {
        return CommandWithRequiredDecls()
    }

    override fun atLongRead(s: ILongRead): CommandWithRequiredDecls<TACCmd.Simple> {
        return CommandWithRequiredDecls(listOf(
            TACCmd.Simple.AssigningCmd.AssignExpCmd(
                lhs = siteVisited,
                rhs = TACSymbol.True.asSym()
            )
        ), setOf(siteVisited))
    }

    override val havocInitVars: List<TACSymbol.Var>
        get() = listOf()
    override val constantInitVars: List<Pair<TACSymbol.Var, ToTACExpr>>
        get() = listOf(siteVisited to TACSymbol.False)

}
