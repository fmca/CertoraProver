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

package rules.sanity

import rules.RuleCheckResult
import solver.SolverResult
import datastructures.stdcollections.*

/**
 * Represents the importance of a [SanityCheckResult].
 * Order is important: later is "worse" than earlier.
 */
enum class SanityCheckResultOrdinal {
    PASSED,
    TIMEOUT,
    UNKNOWN,
    ERROR,
    FAILED;

    infix fun join(other: SanityCheckResultOrdinal) =
        if (this > other) {
            this
        } else {
            other
        }

    fun reportString() =
        when(this) {
            PASSED -> {
                "passed"
            }
            TIMEOUT -> {
                "timeout"
            }
            UNKNOWN -> {
                "unknown"
            }
            ERROR -> {
                "error"
            }
            FAILED -> {
                "failed"
            }
        }


    companion object {
        /**
         * Maps this [RuleCheckResult.Single] into a "default" [SanityCheckResultOrdinal].
         * This mapping function is "default" in the sense that it uses this' [RuleCheckResult.Single.result], and
         * maps [SolverResult.UNSAT] to [FAILED] and [SolverResult.SAT] to [PASSED].
         */
        fun RuleCheckResult.Single.toDefaultSanityCheckResultOrdinal() =
            when (this.result) {
                SolverResult.SAT -> {
                    PASSED
                }
                SolverResult.UNSAT -> {
                    FAILED
                }
                SolverResult.TIMEOUT -> {
                    TIMEOUT
                }
                SolverResult.UNKNOWN -> {
                    UNKNOWN
                }
                SolverResult.SANITY_FAIL -> {
                    throw IllegalArgumentException("Didn't expect to have [SolverResult.SANITY_FAIL]")
                }
            }
    }
}