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

import com.certora.collect.*
import cvlr.CvlrFunctions
import sbf.cfg.*
import sbf.disassembler.*
import sbf.testing.SbfTestDSL
import log.*
import org.junit.jupiter.api.Test
import java.io.ByteArrayOutputStream
import java.io.PrintStream
import org.junit.jupiter.api.*

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@TestMethodOrder(MethodOrderer.OrderAnnotation::class)
@Order(1)
class SimplifyBoolsTest {
    private var outContent = ByteArrayOutputStream()
    private var errContent = ByteArrayOutputStream()

    private val originalOut = System.out
    private val originalErr = System.err

    // system properties have to be set before we load the logger
    @BeforeAll
    fun setupAll() {
        System.setProperty(LoggerTypes.SBF.toLevelProp(), "info")
    }

    // we must reset our stream so that we could match on what we have in the current test
    @BeforeEach
    fun setup() {
        outContent = ByteArrayOutputStream()
        errContent = ByteArrayOutputStream()
        System.setOut(PrintStream(outContent, true)) // for 'always' logs
        System.setErr(PrintStream(errContent, true)) // loggers go to stderr
    }

    private fun debug() {
        originalOut.println(outContent.toString())
        originalErr.println(errContent.toString())
    }

    // close and reset
    @AfterEach
    fun teardown() {
        debug()
        System.setOut(originalOut)
        System.setErr(originalErr)
        outContent.close()
        errContent.close()
    }

    private fun numOfLogicalOr(cfg: SbfCFG): Int {
        var k = 0
        cfg.getBlocks().values.forEach {
            it.getInstructions().forEach {
                if (it is SbfInstruction.Bin && it.op == BinOp.OR) {
                    k++
                }
            }
        }
        return k
    }

    @Test
    fun test1() {
        val cfg = SbfTestDSL.makeCFG("test1") {
            bb(0) {

                select(r2, Condition(CondOp.EQ, Value.Reg(SbfRegister.R3_ARG), Value.Imm(0UL)), 0, 1)
                r1 = 0
                select(r1, Condition(CondOp.EQ, Value.Reg(SbfRegister.R3_ARG), Value.Imm(0UL)), 1, 0)
                r3 = 4
                BinOp.OR(r2,r1)
                assume(CondOp.NE(r2, 1))
                exit()
            }
        }
        sbfLogger.warn{"Before transformation\n$cfg"}
        simplifyBools(cfg)
        sbfLogger.warn{"After transformation\n$cfg"}
        Assertions.assertEquals(true, numOfLogicalOr(cfg) == 0)
    }


    @Test
    fun test2() {
        val cfg = SbfTestDSL.makeCFG("test2") {
            bb(0) {
                CvlrFunctions.CVT_nondet_u64 ()
                r1 = r0
                CvlrFunctions.CVT_nondet_u64 ()
                r2 = r0
                BinOp.OR(r2,r1)
                assume(CondOp.EQ(r2, 0))
                exit()
            }
        }
        sbfLogger.warn{"Before transformation\n$cfg"}
        simplifyBools(cfg)
        sbfLogger.warn{"After transformation\n$cfg"}
        Assertions.assertEquals(true, numOfLogicalOr(cfg) == 0)
    }

    @Test
    fun test3() {
        val cfg = SbfTestDSL.makeCFG("test3") {
            bb(0) {
                CvlrFunctions.CVT_nondet_u64 ()
                r1 = r0
                CvlrFunctions.CVT_nondet_u64 ()
                r2 = r0
                BinOp.OR(r2,r1)
                CvlrFunctions.CVT_nondet_u64 ()
                r3 = r0
                assume(CondOp.EQ(r2, 0))
                exit()
            }
        }
        sbfLogger.warn{"Before transformation\n$cfg"}
        simplifyBools(cfg)
        sbfLogger.warn{"After transformation\n$cfg"}
        Assertions.assertEquals(true, numOfLogicalOr(cfg) == 0)
    }

    @Test
    fun test4() {
        val cfg = SbfTestDSL.makeCFG("test4") {
            bb(0) {
                CvlrFunctions.CVT_nondet_u64 ()
                r1 = r0
                CvlrFunctions.CVT_nondet_u64 ()
                r2 = r0
                BinOp.OR(r2,r1)
                CvlrFunctions.CVT_nondet_u64 ()
                r2 = r0
                assume(CondOp.EQ(r2, 0))
                exit()
            }
        }
        sbfLogger.warn{"Before transformation\n$cfg"}
        simplifyBools(cfg)
        sbfLogger.warn{"After transformation\n$cfg"}
        Assertions.assertEquals(true, numOfLogicalOr(cfg) == 1)
    }

    @Test
    fun test5() {
        val cfg = SbfTestDSL.makeCFG("test5") {
            bb(0) {
                CvlrFunctions.CVT_nondet_u64 ()
                r1 = r0
                CvlrFunctions.CVT_nondet_u64 ()
                r2 = r0
                BinOp.OR(r2,r1)
                CvlrFunctions.CVT_nondet_u64 ()
                r3 = r0
                assume(CondOp.EQ(r2, 0))

                CvlrFunctions.CVT_nondet_u64 ()
                r3 = r0
                CvlrFunctions.CVT_nondet_u64 ()
                r4 = r0
                BinOp.OR(r4,r3)
                CvlrFunctions.CVT_nondet_u64 ()
                r2 = r0
                assume(CondOp.EQ(r4, 0))

                exit()
            }
        }
        sbfLogger.warn{"Before transformation\n$cfg"}
        simplifyBools(cfg)
        sbfLogger.warn{"After transformation\n$cfg"}
        Assertions.assertEquals(true, numOfLogicalOr(cfg) == 0)
    }


    @Test
    fun test6() {
        val cfg = SbfTestDSL.makeCFG("test6") {
            bb(0) {
                select(r2, Condition(CondOp.NE, Value.Reg(SbfRegister.R4_ARG), Value.Imm(0UL)), 0, 1)
                select(r3, Condition(CondOp.NE, Value.Reg(SbfRegister.R4_ARG), Value.Imm(0UL)), 0, 1)
                BinOp.OR(r2,r3)
                select(r3, Condition(CondOp.NE, Value.Reg(SbfRegister.R4_ARG), Value.Imm(0UL)), 1, 0)
                BinOp.OR(r2,r3)
                select(r3, Condition(CondOp.NE, Value.Reg(SbfRegister.R4_ARG), Value.Imm(0UL)), 1, 0)
                BinOp.OR(r2,r3)
                select(r1, Condition(CondOp.LE, Value.Reg(SbfRegister.R3_ARG), Value.Reg(SbfRegister.R9)), 0, 1)
                BinOp.OR(r2,r1)
                assume(CondOp.NE(r2, 1))
                exit()
            }
        }
        sbfLogger.warn{"Before transformation\n$cfg"}
        simplifyBools(cfg)
        sbfLogger.warn{"After transformation\n$cfg"}
        Assertions.assertEquals(true, numOfLogicalOr(cfg) == 0)
    }
}
