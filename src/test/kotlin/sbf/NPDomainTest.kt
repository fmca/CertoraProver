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

import config.ConfigScope
import sbf.analysis.ScalarAnalysis
import sbf.analysis.NPAnalysis
import sbf.cfg.*
import sbf.disassembler.Label
import sbf.disassembler.newGlobalVariableMap
import sbf.testing.SbfTestDSL
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test
import sbf.analysis.AnalysisRegisterTypes
import sbf.domains.*

private val sbfTypesFac = ConstantSbfTypeFactory()
private val top = NPDomain.mkTrue<ScalarDomain<Constant, Constant>, Constant, Constant>()

class NPDomainTest {

    @Test
    fun test01() {
        /*
             *(r10 - 104) := 0
             r3:= *(r10 - 104)
             r2 := r3
             r1 := r2
             assume(r1 == 5)
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r10[-104] = 0
                r3 = r10[-104]
                r2 = r3
                r1 = r2
                assume(CondOp.EQ(r1, 5))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\n newAbsVal=$newAbsVal")
        Assertions.assertEquals(true, newAbsVal.isBottom())
    }

    @Test
    fun test02() {
        /*
             r4 : = 1
             *(r10 - 104) := 1
             r3:= *(r10 - 104)
             r2 := r3
             r2 -= r4
             r1 := r2
             r1 += 1
             assume(r1 == 0)
         */

        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r4 = 1
                r10[-104] = 1
                r3 = r10[-104]
                r2 = r3
                BinOp.SUB(r2, 1)
                r1 = r2
                BinOp.ADD(r1, 1)
                assume(CondOp.EQ(r1, 0))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)

        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\n newAbsVal=$newAbsVal")
        Assertions.assertEquals(true, newAbsVal.isBottom())
    }

    @Test
    fun test03() {
        /*
             r3  := r10 - 96
             *(r10 - 104) := r3
             r2  := *(r10 - 104)
             *r2 := 0
             r1  := *(r10 - 96)
             assume(r1 > 5)
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r3 = r10
                BinOp.SUB(r3, 96)
                r10[-104] = r3
                r2 = r10[-104]
                r2[0] = 0
                r1 = r10[-96]
                assume(CondOp.GT(r1, 5))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\nnewAbsVal=$newAbsVal")
        Assertions.assertEquals(true, newAbsVal.isBottom())
    }

    @Test
    fun test04() {
        /*
             assume(r4 != 0)
             assume(r4 == 0)
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                assume(CondOp.NE(r4, 0))
                assume(CondOp.EQ(r4, 0))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\nnewAbsVal=$newAbsVal")
        Assertions.assertEquals(true, newAbsVal.isBottom())
    }

    @Test
    fun test05() {
        /*
             assume(r4 == 0)
             assume(r4 != 0)
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                assume(CondOp.EQ(r4, 0))
                assume(CondOp.NE(r4, 0))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\nnewAbsVal=$newAbsVal")
        Assertions.assertEquals(true, newAbsVal.isBottom())
    }

    @Test
    fun test06() {
        /*
             assume(r4 == 0)
             assume(r4 > 5)
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                assume(CondOp.EQ(r4, 0))
                assume(CondOp.GT(r4, 5))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\nnewAbsVal=$newAbsVal")
        Assertions.assertEquals(true, newAbsVal.isBottom())
    }

    @Test
    fun test07() {
        /*   // Example where propagation is too weak
             assume(r4 < 3)
             assume(r4 > 5)
         */
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                assume(CondOp.LT(r4, 3))
                assume(CondOp.GT(r4, 5))
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)

        val vFac = VariableFactory()
        val absVal = top
        val b = cfg.getBlock(Label.Address(0))
        check(b!=null)
        val newAbsVal = absVal.analyze(b, vFac, regTypes, false)
        println("absVal=$absVal\n$b\nnewAbsVal=$newAbsVal")
        Assertions.assertEquals(false, newAbsVal.isBottom())
    }

    @Test
    fun test8() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = r10
                BinOp.SUB(r1, 96)
                r2 = r10
                BinOp.SUB(r2, 296)
                br(CondOp.EQ(r3, 0x1), 1, 2)
            }
            bb(1) {
                r4 = r2[16]
                assume(CondOp.EQ(r4, 11))
                goto(3)
            }
            bb(2) {
                r4 = r2[16]
                assume(CondOp.EQ(r4, 7))
                goto(3)
            }
            bb(3) {
                r2[0] = 5
                r3 = 24
                "sol_memcpy_"()
                r4 = r1[16]
                assume(CondOp.EQ(r4, 7))
                r4 = r2[8]
                assume(CondOp.EQ(r4, 10))
                assert(CondOp.EQ(r4, 10)) // added assert so that NPAnalysis runs
                exit()
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val np = NPAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val absValAt1 = np.getPreconditionsAtEntry(Label.Address(1))
        check(absValAt1 != null){"No preconditions for label 1"}
        val absValAt2 = np.getPreconditionsAtEntry(Label.Address(2))
        check(absValAt2 != null){"No preconditions for label 2"}


        println("absVal at 1=$absValAt1\nAbsVal at 2=$absValAt2")
        Assertions.assertEquals(true, absValAt1.isBottom())
        Assertions.assertEquals(false, absValAt2.isBottom())
    }

    @Test
    fun test9() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r2 = r10[-96]
                br(CondOp.NE(r2, 0x1), 1, 2)
            }
            bb(1) {
                assume(CondOp.NE(r2, 0x1))
                r3 = r10[-96]
                assume(CondOp.EQ(r3, 0x1))
                goto(3)
            }
            bb(2) {
                assume(CondOp.EQ(r2, 0x1))
                goto(3)
            }
            bb(3) {
                assert(CondOp.EQ(r4, 0)) // added assert so that NPAnalysis runs
                exit()
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        val np = NPAnalysis(cfg, globals, memSummaries, sbfTypesFac)
        val absValAt1 = np.getPreconditionsAtEntry(Label.Address(1))
        check(absValAt1 != null){"No preconditions for label 1"}
        println("$cfg")
        println("Preconditions at entry of 1=$absValAt1\n")

        Assertions.assertEquals(true, absValAt1.isBottom())
    }

    @Test
    fun test10() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = 1
                br(CondOp.NE(r9, 0x0), 1, 2)
            }
            bb(1) {
                assume(CondOp.NE(r9, 0x0))
                goto(3)
            }
            bb(2) {
                assume(CondOp.EQ(r9, 0x0))
                r1 = 0
                goto(3)
            }
            bb(3) {
                // If we propagate backwards r9 != 0 then this assertion will be always true, which is unsound
                assert(CondOp.NE(r1, 0))
                assume(CondOp.NE(r9, 0))
                BinOp.MUL(r8, r7)
                BinOp.DIV(r8, r9)
                assert(CondOp.NE(r2, 0))  // added unrelated assert so that NPAnalysis starts from here
                exit()
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        println( "$cfg")

        ConfigScope(SolanaConfig.SlicerBackPropagateThroughAsserts, true).use {
            val np = NPAnalysis(cfg, globals, memSummaries, sbfTypesFac)
            val absValAt1 = np.getPreconditionsAtEntry(Label.Address(1))
            check(absValAt1 != null) { "No preconditions for label 1" }
            println( "Preconditions at entry of 1=$absValAt1")
            val absValAt2 = np.getPreconditionsAtEntry(Label.Address(2))
            check(absValAt2 != null) { "No preconditions for label 2" }
            println( "Preconditions at entry of 2=$absValAt2")
            val absValAt3 = np.getPreconditionsAtEntry(Label.Address(3))
            check(absValAt3 != null) { "No preconditions for label 3" }
            println( "Preconditions at entry of 3=$absValAt3")
            Assertions.assertEquals(true, absValAt2.isBottom())
        }
    }

    @Test
    // Same as test10 but disabling SlicerBackPropagateThroughAsserts
    fun test11() {
        val cfg = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                r1 = 1
                br(CondOp.NE(r9, 0x0), 1, 2)
            }
            bb(1) {
                assume(CondOp.NE(r9, 0x0))
                goto(3)
            }
            bb(2) {
                assume(CondOp.EQ(r9, 0x0))
                r1 = 0
                goto(3)
            }
            bb(3) {
                assert(CondOp.NE(r1, 0))
                assume(CondOp.NE(r9, 0))
                BinOp.MUL(r8, r7)
                BinOp.DIV(r8, r9)
                assert(CondOp.NE(r2, 0))  // added assert so that NPAnalysis starts from here
                exit()
            }
        }

        val globals = newGlobalVariableMap()
        val memSummaries = MemorySummaries()
        println("$cfg")

        ConfigScope(SolanaConfig.SlicerBackPropagateThroughAsserts, false).use {
            val np = NPAnalysis(cfg, globals, memSummaries, sbfTypesFac)
            val absValAt1 = np.getPreconditionsAtEntry(Label.Address(1))
            check(absValAt1 != null) { "No preconditions for label 1" }
            println( "Preconditions at entry of 1=$absValAt1")
            val absValAt2 = np.getPreconditionsAtEntry(Label.Address(2))
            check(absValAt2 != null) { "No preconditions for label 2" }
            println( "Preconditions at entry of 2=$absValAt2")
            val absValAt3 = np.getPreconditionsAtEntry(Label.Address(3))
            check(absValAt3 != null) { "No preconditions for label 3" }
            println( "Preconditions at entry of 3=$absValAt3")
            Assertions.assertEquals(false, absValAt2.isBottom())
        }
    }
}


