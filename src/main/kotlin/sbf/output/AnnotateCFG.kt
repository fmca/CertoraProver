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

package sbf.output

import sbf.SolanaConfig
import sbf.analysis.ScalarAnalysis
import sbf.callgraph.SbfCallGraph
import sbf.callgraph.SolanaFunction
import sbf.cfg.*
import sbf.disassembler.Label
import sbf.disassembler.GlobalVariableMap
import sbf.domains.*
import sbf.sbfLogger
import sbf.support.SolanaError
import sbf.support.SolanaInternalError

/**
 * Annotate [cfg] with types extracted from [ScalarAnalysis].
 ***/
fun annotateWithTypes(
    cfg: MutableSbfCFG,
    globals: GlobalVariableMap,
    memSummaries: MemorySummaries) {
    val sbfTypesFac = ConstantSetSbfTypeFactory(SolanaConfig.ScalarMaxVals.get().toULong())
    annotateWithTypes(cfg, globals, memSummaries, sbfTypesFac)
}

/**
 * Annotate the `entrypoint` function with types extracted from [ScalarAnalysis].
 ***/
fun annotateWithTypes(prog: SbfCallGraph, memSummaries: MemorySummaries): SbfCallGraph {
    val sbfTypesFac = ConstantSetSbfTypeFactory(SolanaConfig.ScalarMaxVals.get().toULong())
    return prog.transformSingleEntry { entryCFG ->
        val newEntryCFG = entryCFG.clone(entryCFG.getName())
        annotateWithTypes(newEntryCFG, prog.getGlobals(), memSummaries, sbfTypesFac)
        newEntryCFG
    }
}

/**
 * Only for debugging purposes. We try not to throw any exception from the scalar analysis
 **/
private fun <TNum: INumValue<TNum>, TOffset: IOffset<TOffset>> annotateWithTypes(
        cfg: MutableSbfCFG,
        globals: GlobalVariableMap,
        memSummaries: MemorySummaries,
        sbfTypesFac: ISbfTypeFactory<TNum, TOffset>) {
    try {
        val scalarAnalysis = ScalarAnalysis(cfg, globals, memSummaries, sbfTypesFac)

        for ( (l,_) in cfg.getBlocks()) {
            val absVal = scalarAnalysis.getPre(l)
            if (absVal != null && absVal.isBottom()) {
                val bb = cfg.getMutableBlock(l)
                check(bb!=null)
                bb.add(0,
                    SolanaFunction.toCallInst(
                        SolanaFunction.ABORT,
                        MetaData(Pair(SbfMeta.COMMENT, "Unreachable by scalar analysis"))))
            }
        }

        annotateWithTypes(cfg, scalarAnalysis)
    } catch (e: SolanaError) {
        sbfLogger.info {
            "annotateWithTypes skipped due to some error in the scalar analysis\n" +
            "Here more details about the error:\n" +
            "$e"
        }
    } catch (e: SolanaInternalError) {
        sbfLogger.info {
                "annotateWithTypes skipped due to some error in the scalar analysis\n" +
                "Here more details about the error:\n" +
                "$e"
        }
    }

}

/**
 * Annotate the instructions of [cfg] the with types extracted from [scalarAnalysis].
 **/
private fun <TNum: INumValue<TNum>, TOffset: IOffset<TOffset>> annotateWithTypes(cfg: MutableSbfCFG, scalarAnalysis: ScalarAnalysis<TNum, TOffset>) {
    fun getType(v: Value, absVal: ScalarDomain<TNum, TOffset>): SbfRegisterType? {
        return if (v is Value.Imm) {
            null
        } else {
            absVal.getValue(v).type().concretize()
        }
    }
    fun getPre(block: Label) = scalarAnalysis.getPre(block)

    annotateCFGWithTypes(cfg, scalarAnalysis.globalsMap, scalarAnalysis.memSummaries, ::getPre, ::getType)
}

