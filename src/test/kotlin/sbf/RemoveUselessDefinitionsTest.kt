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

package sbf

import sbf.cfg.*
import sbf.testing.SbfTestDSL
import org.junit.jupiter.api.*

class RemoveUselessDefinitionsTest{

    @Test
    fun test01() {
        println("====== TEST 1  =======")
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                BinOp.ADD(r10, 4096)
                r1 = r10[-56]
                r2 = 5
                exit()
            }
        }
        println("Before transformation\n$cfg")
        removeUselessDefinitions(cfg)
        println("After transformation\n$cfg")
    }

    @Test
    fun test02() {
        println("====== TEST 2  =======")
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                BinOp.ADD(r10, 4096)
                r1 = r10[-56]
                r2 = r1
                exit()
            }
        }
        println("Before transformation\n$cfg")
        removeUselessDefinitions(cfg)
        println("After transformation\n$cfg")
    }
}
