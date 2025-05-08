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

import analysis.maybeNarrow
import tac.MetaKey
import vc.data.CoreTACProgram
import java.util.concurrent.atomic.AtomicInteger
import utils.*
import vc.data.SimplePatchingProgram.Companion.patchForEach
import vc.data.TACCmd
import vc.data.mapMeta
import datastructures.stdcollections.*

/**
 * Numbers all the reads (mload) commands in a program with a number.
 *
 * This is used to correlated `Select` expressions in vc programs back to the original ByteLoad commands.
 */
object MemoryReadNumbering {
    /**
     * A monotonically increasing sequence: the value here does not matter and we don't (I think) care about all the
     * allocator stuff.
     */
    private val idCounter = AtomicInteger(0)

    val READ_COUNTER = MetaKey<Int>("equivalence.read.numbering")

    fun instrument(c: CoreTACProgram): CoreTACProgram {
        return c.parallelLtacStream().mapNotNull {
            it.maybeNarrow<TACCmd.Simple.AssigningCmd.ByteLoad>()
        }.map {
            it to idCounter.getAndIncrement()
        }.patchForEach(c, check = true) { (where, nbr) ->
            replaceCommand(where.ptr, listOf(where.cmd.mapMeta {
                it + (READ_COUNTER to nbr)
            }))
        }
    }
}
