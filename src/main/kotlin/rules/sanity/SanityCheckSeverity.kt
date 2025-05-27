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

import rules.sanity.sorts.SanityCheckSort

/**
 * The "severity" of a [SanityCheckSort] prescribes how to compute the aggregated or summarized result of
 * the underlying sanity-check. Usually, the aggregation of the sanity-results is over sub-rules (or children) of a parametric rule,
 * each of which corresponds to different methods' instantiations.
 *
 * Notably, [Critical] (resp. [Info]) severity level prescribes that the sanity-check of a
 * parametric rule has failed if it has failed for any (rep. for all) of its sub-rules.
 */
sealed class SanityCheckSeverity {


    object Critical : SanityCheckSeverity()

    /**
     * We aggregate independent failures using universal abstraction/quantification
     * for info level sanity checks
     */
    object Info : SanityCheckSeverity()
}
