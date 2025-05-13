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

package vc.data

import algorithms.*
import analysis.*
import analysis.dataflow.*
import analysis.worklist.NaturalBlockScheduler
import utils.*
import java.util.concurrent.ConcurrentHashMap

/**
    A cache for TAC analysis results.

    To create a cacheable analysis, follow this convention:

    ```
    class MyAnalysis private constructor(g: TACCommandGraph) {
        companion object : AnalysisCache.Key<T> {
            fun createCached(g: TACCommandGraph) = MyAnalysis(g)
        }
    }
    ```

    Note the private constructor, to prevent accidental instantiation without the cache.

    To use the cached analysis, you can do:

    ```
    val analysis = program.analysisCache[MyAnalysis]
    ```

    For simple cases where you just have a function whose result you want to cache, you can use the `key` function:

    ```
    val myKey = AnalysisCache.key { graph ->
        // Do some analysis on the graph
        ...
    }

    // use the key
    val result = program.analysisCache[myKey]
    ```
 */
class AnalysisCache(private val lazyGraph: Lazy<TACCommandGraph>) {

    /** A cache key, which knows how to create the corresponding value */
    interface Key<T> {
        fun createCached(graph: TACCommandGraph): T
    }

    /** The actual cache.  Note that values are wrapped in [Lazy], which avoids recursion issues in [computeIfAbsent] */
    private val cache = ConcurrentHashMap<AnalysisCache.Key<*>, Lazy<*>>()

    /** Gets the value associated with [key] from the cache */
    operator fun <T> get(key: AnalysisCache.Key<T>): T =
        cache.computeIfAbsent(key) { lazy { key.createCached(graph) } }.value.uncheckedAs()

    val graph by lazyGraph

    // Convenience properties to get some common analyses
    val def get() = this[LooseDefAnalysis]
    val strictDef get() = this[StrictDefAnalysis]
    val use get() = this[OnDemandUseAnalysis]
    val lva get() = this[LiveVariableAnalysis]
    val gvn get() = this[GlobalValueNumbering]
    val revertBlocks get() = this[RevertBlockAnalysis]
    val domination get() = this[SimpleDominanceAnalysis]
    val reachability get() = this[reachabilityKey]
    val naturalBlockScheduler get() = this[NaturalBlockScheduler]

    companion object {
        /**
            Simple way to create a cache key for a function
         */
        fun <T> key(f: (TACCommandGraph) -> T): AnalysisCache.Key<T> =
            object : AnalysisCache.Key<T> {
                override fun createCached(graph: TACCommandGraph): T = f(graph)
            }

        private val reachabilityKey = AnalysisCache.key { transitiveClosure(it.blockSucc, reflexive = true) }
    }
}
