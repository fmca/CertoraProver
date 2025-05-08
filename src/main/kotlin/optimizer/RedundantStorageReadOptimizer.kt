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

package optimizer

import analysis.LTACCmd
import analysis.LTACCmdView
import analysis.TACCommandGraph
import analysis.narrow
import analysis.worklist.IWorklistScheduler
import analysis.worklist.NaturalBlockScheduler
import analysis.worklist.StepResult
import analysis.worklist.WorklistIteration
import com.certora.collect.*
import datastructures.stdcollections.*
import instrumentation.StoragePackedLengthSummarizer
import tac.NBId
import utils.keysMatching
import utils.mapNotNull
import utils.pointwiseBinopOrNull
import vc.data.*
import verifier.BlockMerger
import java.util.stream.Collector

/**
 * Finds two decodes of a string length (as determined by
 * [instrumentation.StoragePackedLengthSummarizer.StorageLengthReadSummary]) that *must* yield the same decoded value;
 * that is, the underlying "index" (aka, identity) of the string being decoded is the same, and there have been
 * no intervening updates to storage. If this is the case, then, under certain conditions, we can replace the
 * entire decode operation with the already computed result of the decode (if it still exists in some register).
 *
 * This is all necessary because the solidity compiler generates the following:
 * ```
 * l = decode(i)
 * ptr = fp;
 * fp = fp + 32 + l;
 * l2 = decode(i)
 * if l2 == 0 then ... else ...
 * ```
 */
object RedundantStorageReadOptimizer {
    sealed class StorageRead {
        data class LengthDecode(override val index: TACSymbol) : StorageRead()
        data class Direct(override val index: TACSymbol) : StorageRead()
        abstract val index: TACSymbol
    }

    fun optimizeReads(c: CoreTACProgram) : CoreTACProgram {
        val state = mutableMapOf<NBId, TreapMap<TACSymbol.Var, StorageRead>>()
        for(b in c.analysisCache.graph.rootBlocks) {
            state[b.id] = treapMapOf()
        }
        val graph = c.analysisCache.graph

        /**
         * Given a command that holds [instrumentation.StoragePackedLengthSummarizer.StorageLengthReadSummary], determine
         * whether the decoded length is used immediately to allocate a string.
         */
        val success = object : WorklistIteration<NBId, Unit, Boolean>() {
            override val scheduler: IWorklistScheduler<NBId> = NaturalBlockScheduler(graph = c.analysisCache.graph)

            override fun process(it: NBId): StepResult<NBId, Unit, Boolean> {
                val st = state[it]!!.builder()
                val knownIndices = mutableSetOf<TACSymbol.Var>()
                st.mapNotNullTo(knownIndices) {
                    it.value.index as? TACSymbol.Var
                }

                val block = graph.elab(it)
                for(lc in block.commands) {
                    stepCommand(lc, st, knownIndices)
                }
                val work = mutableListOf<NBId>()
                for((dst, cond) in graph.pathConditionsOf(it)) {
                    if(dst in graph.cache.revertBlocks) {
                        continue
                    }
                    val s = if(cond is TACCommandGraph.PathCondition.Summary && cond.s is StoragePackedLengthSummarizer.StorageLengthReadSummary) {
                        if(dst == cond.s.originalBlockStart) {
                            continue
                        }
                        check(dst == cond.s.skipTarget) {
                            "Unexpected destination"
                        }
                        val lengthIndex =  getDecodedIndex(cond.s) ?: return StepResult.StopWith(false)
                        if (lengthIndex != cond.s.outputVar) {
                            st.build() + (cond.s.outputVar to StorageRead.LengthDecode(lengthIndex))
                        } else {
                            st.build()
                        }
                    } else {
                        st.build()
                    }
                    if(dst !in state) {
                        state[dst] = s
                        work.add(dst)
                    } else {
                        val curr = state[dst]!!
                        val join = curr.pointwiseBinopOrNull(s) { a, b ->
                            a.takeIf { it == b }
                        }
                        if(join != curr) {
                            state[dst] = join
                            work.add(dst)
                        }
                    }
                }
                return this.cont(work)
            }

            override fun reduce(results: List<Unit>) : Boolean {
                return true
            }
        }.submit(graph.rootBlocks.map { it.id })
        if(!success) {
            return c
        }
        val rewrites = graph.blocks.parallelStream().mapNotNull {
            val ret = mutableSetOf<RewriteType>()
            val st = state[it.id]?.toMutableMap() ?: return@mapNotNull null
            for(lc in it.commands) {
                if(lc.cmd is TACCmd.Simple.AssigningCmd.WordLoad && lc.cmd.base.meta.find(TACMeta.STORAGE_KEY) != null) {
                    val index = lc.cmd.loc
                    val existing = st.keysMatching { _, storageRead ->
                        storageRead is StorageRead.Direct && storageRead.index == index
                    }.firstOrNull()
                    if(existing != null) {
                        ret.add(RewriteType.AliasVar(
                            where = lc.narrow<TACCmd.Simple.AssigningCmd>(),
                            rhs = existing
                        ))
                    }
                } else if(lc.cmd is TACCmd.Simple.SummaryCmd && lc.cmd.summ is StoragePackedLengthSummarizer.StorageLengthReadSummary && it.commands.size == 1) run {
                    val ind = getDecodedIndex(lc.cmd.summ) ?: return@run
                    val existing = st.keysMatching { _, storageRead ->
                        storageRead is StorageRead.LengthDecode && storageRead.index == ind
                    }.firstOrNull() ?: return@run
                    ret.add(RewriteType.RemoveSummary(
                        rhs = existing,
                        lhs = lc.cmd.summ.outputVar,
                        summaryBlock = it.id,
                        target = lc.cmd.summ.skipTarget
                    ))
                }
                stepCommand(lc = lc, st = st, knownIndices = null)
            }
            ret
        }.collect(Collector.of({
            mutableSetOf<RewriteType>()
        }, { t: MutableSet<RewriteType>, u ->
            t.addAll(u)
        }, { t, u ->
            t.addAll(u)
            t
        }))
        if(rewrites.isEmpty()) {
            return c
        }
        return c.patching { p ->
            for(r in rewrites) {
                when(r) {
                    is RewriteType.AliasVar -> {
                        /* TODO(jtoman): The storage unpacker will break if we do this; sharing storage accesses
                            between an unpacked write and unpacked read breaks a pretty fundamental invariant of the
                            storage unpacker.
                         */
                        /*p.replaceCommand(r.where.ptr, listOf(
                            TACCmd.Simple.AssigningCmd.AssignExpCmd(
                                lhs = r.where.cmd.lhs,
                                rhs = r.rhs.asSym(),
                                meta = r.where.cmd.meta
                            )
                        ))*/
                    }
                    is RewriteType.RemoveSummary -> {
                        p.consolidateEdges(r.target, listOf(r.summaryBlock))
                        p.addBefore(graph.elab(r.target).commands.first().ptr, listOf(
                            TACCmd.Simple.AssigningCmd.AssignExpCmd(
                                lhs = r.lhs,
                                rhs = r.rhs.asSym()
                            )
                        ))
                    }
                }
            }
        }.let(BlockMerger::mergeBlocks)
    }

    private sealed class RewriteType {
        data class AliasVar(val where: LTACCmdView<TACCmd.Simple.AssigningCmd>, val rhs: TACSymbol.Var) : RewriteType()
        data class RemoveSummary(
            val summaryBlock: NBId,
            val lhs: TACSymbol.Var,
            val rhs: TACSymbol.Var,
            val target: NBId
        ) : RewriteType()
    }

    private fun getDecodedIndex(s: StoragePackedLengthSummarizer.StorageLengthReadSummary) : TACSymbol? {
        return when(s.readSort) {
            is StoragePackedLengthSummarizer.SizeReadSort.WordLoad -> s.readSort.indexSym
            is StoragePackedLengthSummarizer.SizeReadSort.UnpackRead -> s.readSort.read.meta.find(TACMeta.SCALARIZATION_SORT)?.let {
                it as? ScalarizationSort.Split
            }?.idx?.asTACSymbol()
        }
    }

    private fun stepCommand(lc: LTACCmd, st: MutableMap<TACSymbol.Var, StorageRead>, knownIndices: MutableSet<TACSymbol.Var>?) {
        if(lc.cmd is TACCmd.Simple.WordStore && lc.cmd.base.meta.find(TACMeta.STORAGE_KEY) != null) {
            st.clear()
        } else if(lc.cmd is TACCmd.Simple.AssigningCmd && lc.cmd.lhs.meta.find(TACMeta.STORAGE_KEY) != null) {
            st.clear()
        } else if(lc.cmd is TACCmd.Simple.AssigningCmd) {
            if(knownIndices != null && lc.cmd.lhs in knownIndices) {
                val eIt = st.entries.iterator()
                while(eIt.hasNext()) {
                    val (k, _) = eIt.next()
                    if(k == lc.cmd.lhs) {
                        eIt.remove()
                    }
                }
            }
            if(lc.cmd is TACCmd.Simple.AssigningCmd.WordLoad && lc.cmd.base.meta.find(TACMeta.STORAGE_KEY) != null && lc.cmd.lhs != lc.cmd.loc) {
                if(lc.cmd.loc is TACSymbol.Var && knownIndices != null) {
                    knownIndices.add(lc.cmd.loc)
                }
                st[lc.cmd.lhs] = StorageRead.Direct(
                    index = lc.cmd.loc
                )
            }
        }
    }
}
