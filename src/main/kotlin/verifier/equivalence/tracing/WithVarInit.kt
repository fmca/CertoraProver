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
package verifier.equivalence.tracing

import datastructures.stdcollections.plus
import tac.Tag
import vc.data.TACSymbol
import vc.data.ToTACExpr

/**
 * Mixin for instrumentation objects which manipulate some set of variables in [allVars]
 * which are initialized with either havoc [havocInitVars] or with expressions [constantInitVars].
 *
 * The initialization of these variables is prepended to the program which is being instrumented automatically.
 */
internal interface WithVarInit {
    val havocInitVars: List<TACSymbol.Var>
    val constantInitVars: List<Pair<TACSymbol.Var, ToTACExpr>>

    val allVars : List<TACSymbol.Var> get() = havocInitVars + constantInitVars.map { it.first }

    /**
     * Helper to generate fresh index variables for mapdefinition expressions (because the stupid call trace
     * *dies* if you reuse one...)
     */
    val idxVar: TACSymbol.Var get() = TACSymbol.Var("certoraMapDefIdx", Tag.Bit256).toUnique("!")
}
