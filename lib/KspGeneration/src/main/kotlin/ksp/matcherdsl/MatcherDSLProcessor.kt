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

package ksp.matcherdsl

import com.google.devtools.ksp.processing.*
import com.google.devtools.ksp.symbol.KSAnnotated
import com.google.devtools.ksp.symbol.KSClassDeclaration
import com.google.devtools.ksp.symbol.Modifier

class MatcherDSLProcessor(private val logger: KSPLogger, private val codeGenerator: CodeGenerator) : SymbolProcessor {
    val nativeTypes = listOf(
        "Int",
        "java.math.BigInteger",
        "vc.data.TACSymbol.Var"
    )

    val siblingMatch = "analysis.ForwardMatcher.SiblingPattern"

    val patternNode = "analysis.ForwardMatcherDSL.PatternNode"

    val commutingOps = listOf(
        "bwand",
        "bwor",
        "eq",
        "add",
        "intAdd",
        "mul",
        "intMul",
        "land",
        "lor"
    )

    val agg = listOf(siblingMatch, patternNode)

    override fun process(resolver: Resolver): List<KSAnnotated> {
        val binExp = resolver.getClassDeclarationByName(resolver.getKSNameFromString("vc.data.TACExpr.BinExp")) ?: return listOf()
        if(resolver.getNewFiles().none {
                it == binExp.containingFile
            }) {
            return listOf()
        }
        val allKinds = sequence {
            binExp.getSealedSubclasses().forEach {
                process(it, resolver)
            }
        }
        val output = codeGenerator.createNewFile(Dependencies(aggregating = true, sources = arrayOf(binExp.containingFile!!)), packageName = "analysis", "ForwardDSLBuilder", "kt").bufferedWriter()
        output.append("""
            package analysis

            object ForwardDSLBuilder {
        """.trimIndent())
        output.newLine()
        for(k in allKinds) {
            val nm = k.simpleName.asString()
            val lowerStart = nm.indexOfFirst {
                it.isLowerCase()
            }
            val builderName = if(lowerStart == -1) {
                nm.lowercase()
            } else {
                nm.substring(0 until lowerStart).lowercase() + nm.substring(lowerStart)
            }
            for(a in agg) {
                val other = listOf(siblingMatch) + nativeTypes
                for(o in other) {
                    val isSiblingBuild = a != patternNode && o != patternNode
                    val pp = { s: String ->
                        if(o in nativeTypes) {
                            "${siblingMatch}.exactly($s)"
                        } else {
                            s
                        }
                    }
                    if(isSiblingBuild) {
                        output.append(generateSiblingBuilder(
                             builderName, k, o, true, pp
                        ))
                        output.newLine()
                        if(o != a) {
                            output.append(generateSiblingBuilder(builderName, k, o, false, pp))
                            output.newLine()
                        }

                    } else {
                        output.append(
                            generatePatternBuilder(builderName, k, o, false, pp)
                        )
                        output.newLine()
                        output.append(
                            generatePatternBuilder(builderName, k, o, true, pp)
                        )
                        output.newLine()
                    }
                }
            }
        }
        output.append("}")
        output.flush()
        output.close()

        return listOf()
    }

    private fun generatePatternBuilder(
        builderName: String,
        ty: KSClassDeclaration,
        otherType: String,
        siblingIsLeft: Boolean,
        pp: (String) -> String
    ): String {
        val klassConst = ty.qualifiedName!!.asString() + "::class.java"
        val (decl, patt, sibling) = if(siblingIsLeft) {
            Triple(
                "$otherType.$builderName(o: $patternNode)",
                "o",
                pp("this")
            )
        } else {
            Triple(
                "$patternNode.$builderName(o: $otherType)",
                "this",
                pp("o")
            )
        }
        val commutes = builderName in commutingOps
        val opType = if(commutes) {
            "analysis.ForwardMatcherDSL.OperandOrder.COMMUTE"
        } else if(siblingIsLeft) {
            "analysis.ForwardMatcherDSL.OperandOrder.SIBLING_LEFT"
        } else {
            "analysis.ForwardMatcherDSL.OperandOrder.SIBLING_RIGHT"
        }
        return """
            infix fun $decl: $patternNode {
                return ForwardMatcherDSL.PatternNode.Intermediate(
                   $patt,
                   $sibling,
                   $opType,
                   $klassConst
                )
            }
        """.trimIndent()
    }



    private fun generateSiblingBuilder(
        builder: String,
        ty: KSClassDeclaration,
        t1: String,
        siblingIsLeft: Boolean,
        f1: (String) -> String
    ) : String {
        val klassConst = ty.qualifiedName!!.asString() + "::class.java"
        val (decl, o1, o2) = if(siblingIsLeft) {
            Triple(
                "$siblingMatch.$builder(o: $t1)",
                "this",
                f1("o")
            )
        } else {
            Triple(
                "$t1.$builder(o: $siblingMatch)",
                f1("this"),
                "o"
            )
        }
        return """
            infix fun $decl: $siblingMatch {
                 return $siblingMatch.Composed(
                     $klassConst,
                     $o1,
                     $o2,
                     ${builder in commutingOps},
                     null
                 )
            }
        """.trimIndent()
    }

    private suspend fun SequenceScope<KSClassDeclaration>.process(it: KSClassDeclaration, res: Resolver) {
        if(Modifier.SEALED in it.modifiers) {
            it.getSealedSubclasses().forEach {
                process(it, res)
            }
            return
        } else if(Modifier.DATA !in it.modifiers) {
            return
        }
        yield(it)
    }

}
