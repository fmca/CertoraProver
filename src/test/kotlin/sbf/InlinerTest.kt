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


import sbf.callgraph.MutableSbfCallGraph
import sbf.disassembler.*
import sbf.domains.*
import sbf.inliner.InlinerConfigFromFile
import sbf.inliner.inline
import sbf.testing.SbfTestDSL
import org.junit.jupiter.api.*

class InlinerTest {

    @Test
    fun test01() {
        println("====== TEST 1 =======")
        /**
         * We just check that this exception is not thrown
        *    "CFG is not well-formed: entrypoint missing exit block After inline+simplify"
        **/
        val entrypoint = SbfTestDSL.makeCFG("entrypoint") {
            bb(0) {
                "foo"()
                "abort"()
                goto(1)
            }
            bb(1) {
               exit()
            }
        }

        val foo = SbfTestDSL.makeCFG("foo") {
            bb(0) {
                "abort"()
                goto(1)
            }
            bb(1) {
                exit()
            }
        }
        entrypoint.normalize()
        foo.normalize()
        entrypoint.verify(true)
        foo.verify(true)

        val globals = newGlobalVariableMap()
        val prog = MutableSbfCallGraph(mutableListOf(entrypoint, foo), setOf("entrypoint"), globals)
        val inlinerConfig = InlinerConfigFromFile(listOf(), listOf())
        val memSummaries = MemorySummaries()
        println("Program\n$prog\n")
        val inlinedProg = inline("entrypoint", prog, memSummaries, inlinerConfig)
        println("Inlined program\n$inlinedProg")
    }

}
