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

package verifier.equivalence

/**
 * A lighter weight map, that is a partial function from a domain
 * of keys [K] to the domain of (non-null) values [V].
 *
 * Unlike the full [Map] interface, there no iteration, enumeration,
 * or more complex operations. Get and contains, that's your lot.
 */
interface PartialFn<K, V: Any> {
    operator fun get(k: K): V?
    operator fun contains(k: K): Boolean = get(k) != null
    companion object {
        fun <K, V: Any> Map<K, V>.inject() = object : PartialFn<K, V> {
            override fun get(k: K): V? {
                return this@inject[k]
            }

        }
    }
}
