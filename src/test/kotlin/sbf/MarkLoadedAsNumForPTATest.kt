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

class MarkLoadedAsNumForPTATest {
    private fun getNumOfMarkedLoads(cfg: SbfCFG): UInt {
        var counter = 0U
        for (b in cfg.getBlocks().values) {
            for (inst in b.getInstructions()) {
                val metadata = inst.metaData
                if (metadata.getVal(SbfMeta.LOADED_AS_NUM_FOR_PTA) != null) {
                    counter++
                }
            }
        }
        return counter
    }

    @Test
    fun test01() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r3 = r10[-200]
                r2 = r3
                br(CondOp.EQ(r2, 0x0), 1, 2)
            }
            bb(1) {
                r2 = 567890
                goto(3)
            }
            bb(2) {
                r2 = 568934
                goto(3)
            }
            bb(3) {
                r2[0] = 5
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        Assertions.assertEquals(true,  getNumOfMarkedLoads(cfg) == 1U)
    }

    @Test
    fun test02() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r3 = r10[-200]
                r2 = r3
                br(CondOp.EQ(r2, 0x0), 1, 2)
            }
            bb(1) {
                assume(CondOp.EQ(r2, 0))
                r2 = 567890
                goto(3)
            }
            bb(2) {
                assume(CondOp.NE(r2, 0))
                r2 = 568934
                goto(3)
            }
            bb(3) {
                r2[0] = 5
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        Assertions.assertEquals(true,  getNumOfMarkedLoads(cfg) == 1U)
    }


    @Test
    fun test03() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r3 = r10[-200]
                r2 = r3
                br(CondOp.EQ(r2, 0x0), 1, 2)
            }
            bb(1) {
                assume(CondOp.EQ(r2, 0))
                r2 = 567890
                goto(3)
            }
            bb(2) {
                assume(CondOp.NE(r2, 0))
                goto(3)
            }
            bb(3) {
                r2[0] = 5
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        Assertions.assertEquals(true,  getNumOfMarkedLoads(cfg) == 0U)
    }

    @Test
    fun test04() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r3 = r10[-200]
                r2 = r3
                br(CondOp.EQ(r2, 0x0), 1, 2)
            }
            bb(1) {
                assume(CondOp.EQ(r2, 0))
                r2 = 567890
                goto(3)
            }
            bb(2) {
                assume(CondOp.NE(r2, 0))
                goto(4)
            }
            bb(4) {
                goto(5)
            }
            bb(5) {
                goto (6)
            }
            bb(6) {
                r2 = 568934
                goto (3)
            }
            bb(3) {
                r2[0] = 5
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        Assertions.assertEquals(true,  getNumOfMarkedLoads(cfg) == 1U)
    }

    @Test
    fun test05() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r3 = r10[-200]
                r2 = r3
                r10[-300] = r3
                br(CondOp.EQ(r2, 0x0), 1, 2)
            }
            bb(1) {
                assume(CondOp.EQ(r2, 0))
                goto(3)
            }
            bb(2) {
                assume(CondOp.NE(r2, 0))
                goto(3)
            }
            bb(3) {
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        Assertions.assertEquals(true,  getNumOfMarkedLoads(cfg) == 0U)
    }

    @Test
    fun test06() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r4 = r10[-200]
                BinOp.LSH(r4, 32)
                BinOp.OR(r4, 24)
                r1 = r4
                BinOp.RSH(r1, 32)
                BinOp.AND(r4, 28)
                assume(CondOp.EQ(r4, 24))
                r10[-300] = r1
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        Assertions.assertEquals(true,  getNumOfMarkedLoads(cfg) == 0U)
    }

    @Test
    // This test shows the limitation of the current implementation.
    fun test07() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r4 = r10[-200]
                BinOp.LSH(r4, 32)
                BinOp.OR(r4, 24)
                r1 = r4
                BinOp.RSH(r1, 32)
                BinOp.AND(r4, 28)
                assume(CondOp.EQ(r4, 24))
                assume(CondOp.EQ(r1, 24))
                exit()
            }
        }
        cfg.normalize()
        println("Before $cfg")
        cfg.verify(true)
        markLoadedAsNumForPTA(cfg)
        println("After $cfg")
        // With an improved implementation, we could mark the load
        Assertions.assertEquals(false,  getNumOfMarkedLoads(cfg) == 1U)
    }
}
