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

import analysis.opt.PatternRewriter.Key.*
import datastructures.stdcollections.*
import vc.data.TACExpr

fun PatternRewriter.solanaPatternsList() = listOf(


    /**
     * `x xor y == 0` ~~> `x == y`
     */
    PatternHandler(
        name = "xor-eq-0",
        pattern = {
            (lSym(A) xor lSym(B)) eq zero
        },
        handle = {
            sym(A) eq sym(B)
        },
        TACExpr.BinRel.Eq::class.java
    ),

    /**
     * `x | y == 0` ~~> `x == 0 && y == 0`
     */
    PatternHandler(
        name = "bworEq0",
        pattern = {
            (lSym(A) bwOr lSym(B)) eq zero
        },
        handle = {
            LAnd(
                Eq(sym(A), Zero),
                Eq(sym(B), Zero),
            )
        },
        TACExpr.BinRel.Eq::class.java
    ),


    )
