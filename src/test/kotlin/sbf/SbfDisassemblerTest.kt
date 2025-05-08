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
import sbf.disassembler.*
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test

class SbfDisassemblerTest {

    @Test
    fun test01() {
        // 0f 21 00 00 00 00 00 00 r1 += r2
        val inst1 = makeAluInst(SbfBytecode.decodeInstruction(8463, true, 0))
        val inst2 = makeAluInst(SbfBytecode.decodeInstruction(1090152584800370688, false, 0))
        println("$inst1 and $inst2")
        Assertions.assertEquals(true, inst1.toString() == inst2.toString())
    }

    @Test
    fun test02() {
        // b7 02 00 00 f9 ff 03 00  r2 = 262137
        val inst1 = makeAluInst(SbfBytecode.decodeInstruction(1125869842072247, true, 0))
        val inst2 = makeAluInst(SbfBytecode.decodeInstruction(-5259641410621078784, false, 0))
        println("$inst1 and $inst2")
        Assertions.assertEquals(true, inst1.toString() == inst2.toString())
        Assertions.assertEquals(true,
        inst1 is SbfInstruction.Bin &&
            inst1.dst.r == SbfRegister.R2_ARG &&
            (inst1.v is Value.Imm &&  (inst1.v as Value.Imm).v ==  262137UL))
    }

    @Test
    fun test03() {
        // 18 02 00 00 f8 ff ff ff    00 00 00 00 fc ff ff ff	r2 = -12884901896 ll
        val bc1 = SbfBytecode.decodeInstruction(-34359737832, true, 0)
        val bc2 = SbfBytecode.decodeInstruction(-17179869184, true, 0)
        val inst = makeLddw(bc1, listOf(bc1,bc2), 0)
        println("$inst")
        Assertions.assertEquals(true,
            inst is SbfInstruction.Bin &&
                inst.dst.r == SbfRegister.R2_ARG &&
                (inst.v is Value.Imm &&  (inst.v as Value.Imm).v == (-12884901896).toULong()))
    }
}
