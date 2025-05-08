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
package instrumentation.transformers

import analysis.CmdPointer
import analysis.opt.FreePointerReadFixupMixin
import analysis.snarrowOrNull
import utils.*
import vc.data.*

/**
  Recognizes the following (in pseudo-tac/evm)
  ```
  x = tacM0x40
  // ...
  LOG x
  z = fp
  ...
  fp = z + e;
  use(x)
  ```

  This can be problematic at allocation analysis time (see [analysis.alloc.ScratchPointerAnalysis]): since x is used and "initialized"
  before the log, the uses of `x` after the LOG look like part of the later allocation, but
  solidity is just reusing stack locations to make my life hard.

  This is a similar problem solved by [analysis.opt.FreePointerReadFixer] but specialized to scratch uses at logs.
 */
object FreePointerAliasLogRewrites : FreePointerReadFixupMixin<FreePointerAliasLogRewrites.Instrumentation> {
    private data class Instrumentation(
        val logSummaryLoc: CmdPointer,
        override val fpAlias: TACSymbol.Var,
    ) : FreePointerReadFixupMixin.ReplacementCandidate {
        override val rewriteUseAfter: CmdPointer
            get() = logSummaryLoc
    }

    fun rewrite(p: CoreTACProgram) : CoreTACProgram {
        val gvn = p.analysisCache.gvn
        val lva = p.analysisCache.lva
        return p.parallelLtacStream().mapNotNull { lc ->
            lc.ptr `to?` lc.snarrowOrNull<TACCmd.EVM.LogCmdSummary>()?.let { summ ->
                when(summ) {
                    is Log0OpcodeSummary -> summ.offset
                    is Log1OpcodeSummary -> summ.offset
                    is Log2OpcodeSummary -> summ.offset
                    is Log3OpcodeSummary -> summ.offset
                    is Log4OpcodeSummary -> summ.offset
                }.let { it as? TACSymbol.Var }?.takeIf { base ->
                    base in gvn.equivBefore(lc.ptr, TACKeyword.MEM64.toVar()) &&
                        lva.isLiveAfter(lc.ptr, base)
                }
            }
        }.map { (loc, alias) ->
            Instrumentation(
                logSummaryLoc = loc,
                fpAlias = alias
            )
        }.doRewrite(p)

    }
}
