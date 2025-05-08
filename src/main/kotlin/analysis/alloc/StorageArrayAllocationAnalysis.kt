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
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package analysis.alloc

import analysis.*
import analysis.alloc.AllocationAnalysis.roundUp
import analysis.smtblaster.Z3BlasterPool
import instrumentation.StorageAllocationDecoder
import parallel.ParallelPool
import parallel.Scheduler
import parallel.forkEvery
import parallel.pcompute
import solver.SolverConfig
import tac.NBId
import utils.*
import vc.data.TACCmd
import vc.data.TACKeyword
import vc.data.TACSymbol
import java.math.BigInteger

/**
 * Find storage array allocations. Despite the name, this object will *technically* find any allocation of an array
 * which matches these (kinda cursed) patterns, but we only see them with storage array copying with via-ir.
 *
 * There are two patterns of note, one for bytes/strings, one for word-sized (in memory) elements. Both have the pattern:
 * ```
 * v = fp;
 * mem[v] = len;
 * out = v + 32
 * // copy len elements into memory starting at 32.
 * // let `end` be the location in memory immediately after the
 * // last element copied
 * L:
 * raw_size = end - v
 * adjusted_size = (raw_size + 31) & ~31
 * fp = v + adjusted_size
 * ```
 * If we can show that `end` is large enough to store a variable of length `len`, then we can classify this as an allocation.
 *
 * (Funnily enough, the copying code above actually ensures that the raw_size is always aligned anyway, but never mind.)
 * `L` is some block at which the copying is known to be complete. This is taken to be the
 * [AllocationAnalysis.Alloc.StorageUnpack.closeLoc] which is used by the [analysis.pta.SimpleInitializationAnalysis] to
 * determine where the init is complete.
 *
 * The actual initialization copying glossed over in the comment about is inferred in the [StorageAllocationDecoder]
 */
object StorageArrayAllocationAnalysis {
    /**
     * Kotlin doesn't have a Quadruple class, so we declare this one.
     * We "seed" this process by searching for the following pattern:
     * `fp = fp + ((var - fp) + 31) & ~31)`
     *
     * [addedFP] is the location of the first read, and [subtractedFp] is the second read, which is subtracted
     * from the (assumed) end pointer for the array block, held in [endPointer]. The location of the subtraction
     * is [subLoc].
     */
    private data class AllocationPatternMatch(
        val addedFP: CmdPointer,
        val subtractedFp: CmdPointer,
        val subLoc: CmdPointer,
        val endPointer: TACSymbol.Var
    )
    private val pattern = PatternDSL.build {
        (TACKeyword.MEM64.toVar().withLocation + roundUp {
            (Var - TACKeyword.MEM64.toVar().withLocation).withAction { subLoc, finalFp, fpReadLoc ->
                Triple(subLoc, finalFp, fpReadLoc)
            }
        }).commute.withAction { _, read, (subLoc, finalFp, fpReadLoc) ->
            AllocationPatternMatch(
                read, fpReadLoc, subLoc = subLoc.ptr, endPointer = finalFp
            )
        }
    }

    /**
     * Information extracted from occurrences of [AllocationPatternMatch] when we think that
     * we have a potential copying described above.
     * [lengthVar] is the `len` variable in the above pseudo-code, and [lenWriteLoc] is
     * the location of that write.
     *
     * [fpAlias] is the value of `v`, the "initial" fp alias (to which `len` is written).
     * [candEndPointer] is the variable `end` in the above, and [targetLoc] is `L`.
     * [fpWriteLoc] is the location where the free pointer is updated.
     *
     * As the class name suggests, the information here is a *candidate*, we is pass to [StorageAllocationDecoder]
     * to verify that the code in between the length write and the fp update actually allocates an array.
     */
    private data class StorageAllocCand(
        val lengthVar: TACSymbol.Var,
        val lenWriteLoc: CmdPointer,
        val fpAlias: TACSymbol.Var,
        val candEndPointer: TACSymbol.Var,
        val targetLoc: NBId,
        val fpWriteLoc: CmdPointer
    )

    /**
     * The "finalized" storage array allocation, which has been validated by [StorageAllocationDecoder];
     * [initCloseBlock] is L, [fpWriteLoc] is the fp update, [lengthVar] is the length and location of the array length,
     * and [elemSize] is the inferred element size.
     */
    data class StorageUnpackingInit(
        val initCloseBlock: NBId,
        val fpWriteLoc: CmdPointer,
        val lengthVar: Pair<CmdPointer, TACSymbol.Var>,
        val elemSize: BigInteger
    )

    private fun analyze(g: TACCommandGraph, matcher: SymbolQuery<PatternMatcher.ConstLattice<AllocationPatternMatch>>, blasterPool: Z3BlasterPool) : List<StorageUnpackingInit> {
        // find fp updates
        return g.commands.parallelStream().mapNotNull {
            it.maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.takeIf {
                it.cmd.lhs == TACKeyword.MEM64.toVar()
            }
        // find matches
        }.mapNotNull {
            it.ptr `to?` matcher.queryFrom(it).toNullableResult()
        // ensure that we are adding and subtracting from the same thing
        }.filter { (_, holder) ->
            holder.addedFP == holder.subtractedFp && g.elab(holder.addedFP).maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>() != null
        /*
         * Ensure that the value we are subtracting from has the same value at the start of the block where the subtraction occurs,
         * i.e. `end` isn't somehow redefined in L.
         */
        }.mapNotNull { (w, holder) ->
            val subBlock = holder.subLoc.block
            val target = CmdPointer(subBlock, 0)
            val endTarget = g.cache.gvn.findCopiesAt(
                target,
                source = holder.subLoc to holder.endPointer
            ).firstOrNull {
                g.cache.lva.isLiveBefore(ptr = target, v = it)
            } ?: return@mapNotNull null
            w to holder.copy(
                endPointer = endTarget
            )
        }.flatMap { (write, allocWithSub) ->
            /**
             * Extract the candidates. Find a write into memory at the freshly read free pointer which is writing a length;
             * this is the length write mentioned above.
             */
            val fpAlias = g.elab(allocWithSub.addedFP).narrow<TACCmd.Simple.AssigningCmd>().cmd.lhs
            g.cache.use.useSitesAfter(fpAlias, pointer = allocWithSub.addedFP).mapNotNull { fpUseSite ->
                g.elab(fpUseSite).maybeNarrow<TACCmd.Simple.AssigningCmd.ByteStore>()?.takeIf {
                    it.cmd.loc == fpAlias && it.cmd.value is TACSymbol.Var
                }
            }.map {
                StorageAllocCand(
                    lengthVar = it.cmd.value as TACSymbol.Var,
                    fpAlias = fpAlias,
                    targetLoc = allocWithSub.subLoc.block,
                    candEndPointer = allocWithSub.endPointer,
                    lenWriteLoc = it.ptr,
                    fpWriteLoc = write
                )
            }.stream()
        }.toList().forkEvery { storageAllocCand: StorageAllocCand ->
            /**
             * For each of these, run the storage allocation decoder. The [StorageAllocationDecoder]
             * returns a non-null elem size on a match, so we filter on that.
             */
            Scheduler.compute {

                storageAllocCand to StorageAllocationDecoder(
                    graph = g,

                    start = storageAllocCand.lenWriteLoc,
                    fpAlias = storageAllocCand.fpAlias,
                    arrayLen = storageAllocCand.lengthVar,

                    solvers = blasterPool,
                    endVar = storageAllocCand.candEndPointer,
                    endLoc = storageAllocCand.targetLoc,
                )
            }
        }.pcompute().let {
            ParallelPool.runInherit(it, spawnPolicy = ParallelPool.SpawnPolicy.GLOBAL)
        }.filter { (_, elemSize) ->
            // non-null elem size -> successful copy
            elemSize != null
        }.map { (cand, sz) ->
            StorageUnpackingInit(
                fpWriteLoc = cand.fpWriteLoc,
                initCloseBlock = cand.targetLoc,
                lengthVar = cand.lenWriteLoc to cand.lengthVar,
                elemSize = sz!!
            )
        }
    }

    fun analyze(g: TACCommandGraph) : List<StorageUnpackingInit> {
        val matcher = PatternMatcher.compilePattern(g, pattern)
        return ParallelPool.allocInScope(2000 to SolverConfig.cvc5.bv, { (ts, config) -> Z3BlasterPool(z3TimeoutMs = ts, solverConfig = config)}) {
            analyze(g, matcher, it)
        }
    }
}
