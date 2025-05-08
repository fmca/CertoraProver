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

class TACMulTest {

    @Test
    fun test01() {
        /*
	       r1 := r10
	       r1 := r1 - 100
	       r2 := 5
	       r3 := 0
	       r4 := 7
	       r5 := 0
	       call __multi3(r1,r2,r3,r4)
	       r2 := *(u64 *) (r1 + 0)
	       r3 := *(u64 *) (r1 + 8)
	       assert(r2 == 35)
	       assert(r3 == 0)
         */

        val cfg = SbfTestDSL.makeCFG("test1") {
            bb(0) {
                r1 = r10
                BinOp.SUB(r1, 100)
                r2 = 5
                r3 = 0
                r4 = 7
                r5 = 0
                "__multi3"()
                r2 = r1[0]
                r3 = r1[8]
                assert(CondOp.EQ(r2, 35UL))
                assert(CondOp.EQ(r3, 0UL))
                exit()
            }
        }

        cfg.normalize()
        cfg.verify(true)

        println("$cfg")
        val tacProg = toTAC(cfg)
        println(dumpTAC(tacProg))
        Assertions.assertEquals(true, verify(tacProg))
    }

}
