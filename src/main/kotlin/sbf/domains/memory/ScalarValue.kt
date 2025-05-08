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

package sbf.domains

import sbf.cfg.*
import sbf.disassembler.*

typealias ConstantNum = Constant
typealias ConstantOffset = Constant

/**
 * An "abstract" version of [SbfRegisterType], that extends it with top/bot elements and
 * lattice operations such as join and inclusion
 *
 *             ----------------- Top
 *           /                    |
 *          /         -------- Pointer ---------
 *        /         /          |         |      \
 *      Num       Stack     Input    Heap   Global
 *        \            \      |        /       /
 *          -------------- Bottom -------------
 *  where
 *  - Top: any type
 *  - Bottom: type error
 *  - Num: number
 *  - Stack: pointer to the stack (i.e., it contains a stack offset)
 *  - Input: pointer to the input region
 *  - Heap: pointer to the heap (i.e, an integer between [0x300000000, 0x3000077f8])
 *  - Global: pointer to a global variable
 **/
sealed class SbfType {
    // To represent type errors
    object Bottom : SbfType() {
        override fun toString(): String {
            return "bottom"
        }
    }

    // Any type
    object Top : SbfType() {
        override fun toString(): String {
            return "top"
        }
    }

    // Numerical type
    data class NumType(val value: ConstantNum): SbfType() {

        /**
         *  Cast a number to a pointer only if the number is a valid heap address or the address of a global variable.
         *  We don't try to cast a number to a pointer if the number can be a valid address in the stack or input regions.
         *  In that case, we will return null.
         **/
        fun castToPtr(globalsMap: GlobalVariableMap): PointerType? {
            fun findLowerBound(key: Long): Pair<Long, SbfGlobalVariable>? {
                // globalsMap is sorted
                var lb: Pair<Long, SbfGlobalVariable> ? = null
                for (kv in globalsMap) {
                    if (kv.key <= key) {
                        lb = Pair(kv.key, kv.value)
                    } else {
                        break
                    }
                }
                return lb
            }

            val n = value.get()
            if (n != null) {
                if (n in SBF_HEAP_START until SBF_HEAP_END) {
                    val offset = n - SBF_HEAP_START
                    check(offset >= 0) {"Offsets of pointers to the Heap region heap cannot be negative"}
                    return PointerType.Heap(ConstantOffset(offset))
                } else {
                    // We check if n can be a valid address assigned to a global variable.
                    val lb = findLowerBound(n)
                    if (lb != null) {
                        val globalVar = lb.second
                        if (globalVar.size == 0L) {
                            // The global might have been inferred by GlobalInferenceAnalysis.
                            // We assume that offset is the start of the global
                            val offset = ConstantOffset(n)
                            return PointerType.Global(offset, globalVar)
                        }
                        else if (n >= globalVar.address && (n < (globalVar.address + globalVar.size))) {
                            // Note that in case of an array, `offset` might not be the start address of the global.
                            // That is, it's not always true that offset == globalVar.address
                            val offset = ConstantOffset(n)
                            return PointerType.Global(offset, globalVar)
                        }
                    }
                }
            }
            /// We are here if the number cannot be either the address of a global or a valid address
            /// in the heap.
            return null
        }


        override fun toString(): String {
            return if (value.isTop()) {
                "num"
            } else {
                "num($value)"
            }
        }
    }

    // Pointer type
    sealed class PointerType: SbfType() {
        abstract val offset : ConstantOffset
        abstract fun withOffset(newOffset: ConstantOffset): PointerType

        fun samePointerType(other: PointerType) = this::class == other::class

        data class Stack(override val offset: ConstantOffset): PointerType() {
            override fun toString(): String {
                return "sp($offset)"
            }
            override fun withOffset(newOffset: ConstantOffset) = Stack(newOffset)
        }

        data class Input(override val offset: ConstantOffset): PointerType() {
            override fun toString(): String {
                return "input($offset)"
            }
            override fun withOffset(newOffset: ConstantOffset) = Input(newOffset)
        }

        data class Heap(override val offset: ConstantOffset): PointerType() {
            override fun toString(): String {
                return "heap($offset)"
            }
            override fun withOffset(newOffset: ConstantOffset) = Heap(newOffset)
        }

        // global.address is the start address of the global variable.
        // offset is actually an absolute address between [global.address, global.address+size)
        data class Global(override val offset: ConstantOffset,
                          val global: SbfGlobalVariable?): PointerType() {
            override fun toString(): String {
                return if (global != null) {
                    if (global is SbfConstantStringGlobalVariable) {
                        "global($global)"
                    } else {
                        "global(${global.name}, $offset)"
                    }
                } else {
                    "global($offset)"
                }
            }
            override fun withOffset(newOffset: ConstantOffset) = Global(newOffset, global)
        }
    }

    fun join(other: SbfType): SbfType {
        if (this is Bottom) {
            return other
        } else if (other is Bottom) {
            return this
        } else if (this is Top || other is Top) {
            return Top
        }

        return if (this is NumType && other is NumType) {
            NumType(value.join(other.value))
        } else if (this is PointerType.Stack && other is PointerType.Stack) {
            PointerType.Stack(offset.join(other.offset))
        } else if (this is PointerType.Input && other is PointerType.Input) {
            PointerType.Input(offset.join(other.offset))
        } else if (this is PointerType.Heap && other is PointerType.Heap) {
            PointerType.Heap(offset.join(other.offset))
        } else if (this is PointerType.Global && other is PointerType.Global) {
            PointerType.Global(offset.join(other.offset),
                if (global == other.global) {
                    global
                } else {
                    null
                })
        } else {
            Top
        }
    }

    fun lessOrEqual(other: SbfType): Boolean {
        if (other is Top || this is Bottom) {
            return true
        } else if (this is Top || other is Bottom) {
            return false
        }

        return if (this is NumType && other is NumType) {
            value.lessOrEqual(other.value)
        } else if (this is PointerType.Stack && other is PointerType.Stack) {
            offset.lessOrEqual(other.offset)
        } else if (this is PointerType.Input && other is PointerType.Input) {
            offset.lessOrEqual(other.offset)
        } else if (this is PointerType.Heap && other is PointerType.Heap) {
            offset.lessOrEqual(other.offset)
        } else if (this is PointerType.Global && other is PointerType.Global) {
            offset.lessOrEqual(other.offset)
        } else {
            false
        }
    }

    fun concretize(): SbfRegisterType? {
        return when (this) {
            is Top, is Bottom -> null
            is NumType -> SbfRegisterType.NumType(this.value)
            is PointerType -> {
                when (this) {
                    is PointerType.Stack -> SbfRegisterType.PointerType.Stack(this.offset)
                    is PointerType.Input -> SbfRegisterType.PointerType.Input(this.offset)
                    is PointerType.Heap -> SbfRegisterType.PointerType.Heap(this.offset)
                    is PointerType.Global -> SbfRegisterType.PointerType.Global(this.offset, this.global)
                }
            }
        }
    }
}

/**
 * This class wraps [SbfType] inside [StackEnvironmentValue] which is an interface.
 * It represents the value stored in a register or stack offset.
 **/
class ScalarValue(private val type: SbfType): StackEnvironmentValue<ScalarValue> {
    companion object {
        fun mkTop() = ScalarValue(SbfType.Top)
        fun mkBottom() = ScalarValue(SbfType.Bottom)
        fun from(value: ULong): ScalarValue {
            // REVISIT: immediate values are represented as ULong
            // The analysis uses signed integer semantics, so we need to convert the value to Long.
            // Therefore, overflow will happen if value represents a negative number.
            return ScalarValue(SbfType.NumType(Constant(value.toLong())))
        }
        fun from(value: Long) = ScalarValue(SbfType.NumType(Constant(value)))

        fun anyNum() = ScalarValue(SbfType.NumType(Constant.makeTop()))
    }

    fun get() = type
    override fun isBottom() = type is SbfType.Bottom
    override fun isTop() = type is SbfType.Top
    override fun mkTop() = ScalarValue(SbfType.Top)
    override fun join(other: ScalarValue) = ScalarValue(type.join(other.type))
    override fun widen(other: ScalarValue)= ScalarValue(type.join(other.type))
    override fun lessOrEqual(other: ScalarValue) = type.lessOrEqual(other.type)
    override fun toString() = type.toString()
}
