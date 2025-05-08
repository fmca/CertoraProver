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
import sbf.analysis.AnalysisRegisterTypes

data class ScalarAnalysisCheck<TNum: INumValue<TNum>, TOffset: IOffset<TOffset>>(
        /** the assertion **/
        val locInst: LocatedSbfInstruction,
        /** whether the assertion is proven **/
        val result: Boolean,
        /** the results of the analysis just before the assertion **/
        val invariants: ScalarDomain<TNum, TOffset>
        ) {
    init {
        check(locInst.inst is SbfInstruction.Assert)
    }
}


class  ScalarAnalysisProver<TNum: INumValue<TNum>, TOffset: IOffset<TOffset>>(
        private val cfg: SbfCFG,
        private val vfac: ISbfTypeFactory<TNum, TOffset>,
        private val memSummaries: MemorySummaries = MemorySummaries(),
        private val globals: GlobalVariableMap = newGlobalVariableMap()
) {
    val checks = mutableListOf<ScalarAnalysisCheck<TNum, TOffset>>()

    init {  run() }

    private fun run() {
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, vfac)
        val regTypes = AnalysisRegisterTypes(scalarAnalysis)
        for (b in cfg.getBlocks().values) {
            for (locInst in b.getLocatedInstructions()) {
                val inst = locInst.inst
                if (inst is SbfInstruction.Assert) {
                    val x = ScalarDomain.makeTop(vfac)
                    for (use in inst.readRegisters) {
                        val scalarVal = ScalarValue(regTypes.typeAtInstruction(locInst, use.r))
                        x.setRegister(use, scalarVal)
                    }
                    if (x.isBottom()) {
                        checks.add(ScalarAnalysisCheck(locInst, true, x))
                    } else {
                        val y = x.deepCopy()
                        y.analyzeAssume(inst.cond.negate())
                        if (y.isBottom()) {
                            checks.add(ScalarAnalysisCheck(locInst, true, x))
                        } else {
                            checks.add(ScalarAnalysisCheck(locInst, false, x))
                        }
                    }
                }
            }
        }
    }

    fun check(locInst: LocatedSbfInstruction): Boolean {
        val proverCheck = checks.find { it.locInst == locInst}
        check(proverCheck != null) {"ScalarAnalysisProver cannot find inst $locInst"}
        return proverCheck.result
    }

    override fun toString(): String {
        val sb = StringBuilder()
        for (check in checks) {
            sb.append("${check.locInst.inst}: ${check.result} -- Invariants:${check.invariants}\n")
        }
        return sb.toString()
    }
}
