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

class TACShrTest {

    @Test
    fun test1() {
        /**
         * This code is generated from
         *  ```
         *  let x:i64 = nondet()
         *  cvt_assume(x>=0)
         *  cvt_assume(x< i64::max())
         *  ```
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r2 = r1
                BinOp.XOR(r1, -1)
                BinOp.ARSH(r1, 63)
                assume(CondOp.EQ(r1, 1UL))        // assume MSB(r1) == 0 (i.e., positive number)
                assume(CondOp.LT(r2, Long.MAX_VALUE))  // assume r1 < MAX
                r3 = 1
                assert(CondOp.EQ(r3, 0)) // assert(false)
                exit()
            }
        }
        println("$cfg")
        val tacProg = toTAC(cfg)
        println(dumpTAC(tacProg))
        Assertions.assertEquals(false, verify(tacProg))
    }


}
