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

package sbf.domains

interface IOffset<V> {
    // Return null if the offset cannot be expressed as a signed long
    fun get(): Long?

    /* Numerical operations */
    fun add(other: V): V
    fun add(n: Long): V
    fun sub(other: V): V
    fun sub(n: Long): V
    fun mul(other: V): V
    fun mul(n: Long): V

    /* lattice operations */
    fun isTop(): Boolean
    fun isBottom(): Boolean
    fun join(other: V): V
    fun widen(other: V): V
    fun meet(other: V): V
    fun lessOrEqual(other: V): Boolean

    override fun toString(): String
}
