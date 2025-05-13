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

package tac.generation

import analysis.*
import config.*
import datastructures.stdcollections.*
import instrumentation.transformers.TACDSA
import kotlin.streams.*
import tac.generation.*
import utils.*
import vc.data.*
import verifier.*

/**
    Base class for assigning summaries that run after unrolling.  We materialize all of these in [materialize].
*/
@KSerializable
public abstract class PostUnrollAssignmentSummary : AssignmentSummary() {
    override val annotationDesc get() = "post-unroll assignment"

    override val mayWriteVars = listOf<TACSymbol.Var>()

    /** Materialize this summary, given the simplified inputs. */
    abstract protected fun gen(
        simplifiedInputs: List<TACExpr>,
        analysisCache: AnalysisCache,
    ): CommandWithRequiredDecls<TACCmd.Simple>

    companion object {
        fun materialize(prog: CoreTACProgram) =
            prog.patching { patch ->
                val constAnalysis = MustBeConstantAnalysis(
                    prog.analysisCache.graph,
                    NonTrivialDefAnalysis(prog.analysisCache.graph)
                )
                fun TACSymbol.simplifyAt(where: CmdPointer) =
                    constAnalysis.mustBeConstantAt(where, this)?.let { it.asTACExpr } ?: this.asSym()

                // Note: it's important not to use a parallel stream here, as it can create recursion issues with the
                // analysis cache.
                val replacements = prog.ltacStream().mapNotNull { lcmd ->
                    lcmd.snarrowOrNull<PostUnrollAssignmentSummary>()?.let { op ->
                        lcmd.ptr to op.gen(
                            op.inputs.map { it.simplifyAt(lcmd.ptr) },
                            prog.analysisCache
                        )
                    }
                }.asSequence()

                for ((ptr, impl) in replacements) {
                    patch.replaceCommand(ptr, impl)
                }
            }.let {
                // We introduce new variables, so we should re-run DSA.
                CoreToCoreTransformer(ReportTypes.DSA, TACDSA::simplify).applyTransformer(it)
            }
    }
}
