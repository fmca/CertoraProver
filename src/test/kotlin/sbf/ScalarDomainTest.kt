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

import sbf.analysis.ScalarAnalysis
import sbf.cfg.*
import sbf.disassembler.*
import sbf.domains.*
import sbf.testing.SbfTestDSL
import org.junit.jupiter.api.*
import sbf.analysis.AnalysisRegisterTypes

private val sbfTypesFac = ConstantSbfTypeFactory()
private val env = StackEnvironment<ScalarValue<Constant, Constant>>()

class ScalarDomainTest {

    @Test
    fun test01() {
        println( "====== TEST 1: StackEnvironment.overlap  =======")
        // check [20,28) is included [4,28)
        Assertions.assertEquals(true, env.overlap(ByteRange(20, 8), 4, 24, true))
        // check [24,32) is included in [4,28)
        Assertions.assertEquals(false, env.overlap(ByteRange(24, 8), 4, 24, true))
        // check [24,32) overlaps with [4,28)
        Assertions.assertEquals(true, env.overlap(ByteRange(24, 8), 4, 24, false))
        // check [28,36) overlaps with [4,28)
       Assertions.assertEquals(false, env.overlap(ByteRange(28, 8), 4, 24, false))
        // check [4,12) is included in [12,44]
        Assertions.assertEquals(false, env.overlap(ByteRange(4, 8), 12, 32, true))
        // check [8,16) overlaps with [12,44]
        Assertions.assertEquals(true, env.overlap(ByteRange(8, 8), 12, 32, false))
        // check [8,16) is included in [12,44]
        Assertions.assertEquals(false, env.overlap(ByteRange(8, 8), 12, 32, true))
    }

    @Test
    fun test02() {
        println( "====== TEST 2: memcpy (last word)  =======")
        /**
         *   r2 := r10 - 104
         *   *(r2 + 0):= 0
         *   *(r2 + 8):= 0
         *   *(r2 + 16):= 0
         *   *(r2 + 24):= 0
         *   r1 := r10 - 204
         *   r3 := 32
         *   memcpy(r1,r2,r3)
         *   assert(*(r1+24) == 0)
        **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r2 = r10
                BinOp.SUB(r2, 104)
                r1 = r10
                BinOp.SUB(r1, 204)
                r2[0] = 0
                r2[8] = 0
                r2[16] = 0
                r2[24] = 0
                r3 = 32
                "sol_memcpy_"()
                r4 = r1[24]
                assert(CondOp.EQ(r4, 0))
            }
        }
        println("$cfg")
        val prover = ScalarAnalysisProver(cfg, sbfTypesFac)
        for (check in prover.checks) {
            Assertions.assertEquals(true, check.result)
        }
    }

    @Test
    fun test03() {
        println( "====== TEST 3  =======")
        /**
         *   r1 := 5
         *   r1 := r1 + 5
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = 5
                BinOp.ADD(r1, 5)
            }
        }
        println("$cfg")
        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val b0 = cfg.getBlock(Label.Address(0))
        check (b0 != null)
        val addInst = b0.getLocatedInstructions().drop(1).first()
        val type = regTypes.typeAtInstruction(addInst, SbfRegister.R1_ARG)
        Assertions.assertEquals(true, type is SbfType.NumType && type.value.get() == 5L)
    }

    @Test
    fun test04() {
        println( "====== TEST 4  =======")
        /**
         *   assume(r1 == 5)
         *   assert(r1 == 5)
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                assume(CondOp.EQ(r4, 5))
                assert(CondOp.EQ(r4, 5))
            }
        }
        println("$cfg")
        val prover = ScalarAnalysisProver(cfg, sbfTypesFac)
        for (check in prover.checks) {
            Assertions.assertEquals(true, check.result)
        }
    }

    @Test
    fun test05() {
        println( "====== TEST 5: simple memory store and read =======")
        /**
         *   r1 := r10 - 104
         *   *(r1+0) = 5
         *   assert( *(r1+0) == 5)
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = r10
                BinOp.SUB(r1, 104)
                r1[0] = 5
                r1 = r1[0]
                assert(CondOp.EQ(r1, 5))
            }
        }
        println("$cfg")
        val prover = ScalarAnalysisProver(cfg, sbfTypesFac)
        for (check in prover.checks) {
            Assertions.assertEquals(true, check.result)
        }
    }

    @Test
    fun test06() {
        println( "====== TEST 6: implicit cast at memory store  =======")
        /**
         *   r1 == 56789
         *   *(r1+0) = 0
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = 56789
                r1[0] = 0
            }
        }
        println("$cfg")
        val globals: GlobalVariableMap = newGlobalVariableMap(56789L to SbfGlobalVariable("myglobal", 56789, 8))
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val b0 = cfg.getBlock(Label.Address(0))
        check (b0 != null)
        val secondInst = b0.getLocatedInstructions().drop(1).first()
        val secondType = regTypes.typeAtInstruction(secondInst, SbfRegister.R1_ARG)
        println("$secondInst -> $secondType")
       // Assertions.assertEquals(true, secondType is SbfType.NumType && secondType.value.get() == 5L)
    }

    @Test
    fun test07() {
        println( "====== TEST 7: implicit cast at memory read  =======")
        /**
         *   r1 == 56789
         *   r1 = *(r1+0)
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = 56789
                r1[0] = 0
            }
        }
        println("$cfg")
        val globals: GlobalVariableMap = newGlobalVariableMap(56789L to SbfGlobalVariable("myglobal", 56789, 8))
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val b0 = cfg.getBlock(Label.Address(0))
        check (b0 != null)
        val secondInst = b0.getLocatedInstructions().drop(1).first()
        val secondType = regTypes.typeAtInstruction(secondInst, SbfRegister.R1_ARG)
        println("$secondInst -> $secondType")
        // Assertions.assertEquals(true, secondType is SbfType.NumType && secondType.value.get() == 5L)
    }

    @Test
    fun test08() {
        println( "====== TEST 8 =======")
        /**
         *  Example where the content of a stack offset is written and then copied (via memcpy) to another part of the stack.
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r4 = r10
                BinOp.SUB(r4, 104)
                r4[0] = 5  // *sp(-104) := 5

                r2 = r10
                BinOp.SUB(r2, 504)
                r2[0] = r4

                r3 = 8
                r1 = r10
                BinOp.SUB(r1, 204)
                "sol_memcpy_"()
                r5 = r1[0]
                r5 = r5[0]
                assert(CondOp.EQ(r5, 5))
                exit()
            }
        }
        println("$cfg")
        val prover = ScalarAnalysisProver(cfg, sbfTypesFac)
        for (check in prover.checks) {
            Assertions.assertEquals(true, check.result)
        }
    }


    @Test
    fun test09() {
        println( "====== TEST 9: two stores that overlap  =======")
        /**
         *   r1 := r10 - 104
         *   *(r1+0) = 5
         *   *(r1+4) = 10
         *   assert( *(r1+0) == 5) // it shouldn't be probable
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = r10
                BinOp.SUB(r1, 104)
                r1[0] = 5
                r1[4] = 10
                r1 = r1[0]
                assert(CondOp.EQ(r1, 5))
            }
        }
        println("$cfg")
        val prover = ScalarAnalysisProver(cfg, sbfTypesFac)
        for (check in prover.checks) {
            Assertions.assertEquals(false, check.result)
        }
    }

    @Test
    fun test10() {
        println( "====== TEST 10: two contiguous stores with no overlaps  =======")
        /**
         *   r1 := r10 - 104
         *   *(r1+0) = 5
         *   *(r1+8) = 10
         *   assert( *(r1+8) == 10) // it's true
         **/

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = r10
                BinOp.SUB(r1, 104)
                r1[0] = 5
                r1[8] = 10
                r1 = r1[8]
                assert(CondOp.EQ(r1, 10))
            }
        }
        println("$cfg")
        val prover = ScalarAnalysisProver(cfg, sbfTypesFac)
        for (check in prover.checks) {
            Assertions.assertEquals(true, check.result)
        }
    }

}
