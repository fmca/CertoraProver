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

package sbf.cfg

/**
 * We search for code patterns that correspond to Rust `checked_add` or `saturating_add`:
 *  ```
 *   z = x + y
 *   if x > z then ...
 * ```
 *
 * If the pattern is found, then we mark the addition and the condition instructions with the
 * following metadata:
 *
 *  ```
 *   z = x + y /*add.overflow*/
  *  if x > z  /*promoted add.overflow check: z > 2^64*/ then ...
 * ```
 *
 * The metadata is only used during TAC encoding.
 */

fun markAddWithOverflow(cfg: MutableSbfCFG) {
    // normalize select to make simpler `markAddWithOverflow`
    cfg.getMutableBlocks().values.forEach { bb ->
        bb.getLocatedInstructions().forEach { locInst ->
            normalizeSelect(bb, locInst)
        }
    }

    cfg.getMutableBlocks().values.forEach { bb ->
        bb.getLocatedInstructions().forEach { locInst ->
            val inst = locInst.inst
            if (inst is SbfInstruction.Bin && inst.op == BinOp.ADD) {
                markAddWithOverflow(cfg, locInst)
            }
        }
    }
}

/** Replace `select(cond, 0, 1)` with `select(neg(cond), 1, 0)` **/
private fun normalizeSelect(bb: MutableSbfBasicBlock, locInst: LocatedSbfInstruction) {
    val inst = locInst.inst
    if (inst is SbfInstruction.Select) {
        val trueV = inst.trueVal
        val falseV = inst.falseVal
        if (trueV is Value.Imm && falseV is Value.Imm) {
            if (trueV.v == 0UL && falseV.v == 1UL) {
                val normSelect = inst.copy(cond = inst.cond.negate(), trueVal = falseV, falseVal = trueV)
                bb.replaceInstruction(locInst.pos, normSelect)
            }
        }
    }
}

/**
 *  It searches for one of these two patterns:
 *
 *  ```
 *  r3 = r4
 *  r3 = r3 + r2
 *  r3 = r3 - 1 // optional
 *  r2 = select(r4 ugt r3, 1, 0)
 *  ```
 *  or
 *  ```
 *  r3 = r4
 *  r3 = r3 + r2
 *  r3 = r3 - 1 // optional
 *  if (r4 ugt r3)
 *  ```
 *
 *  For simplicity, all instructions must be in the same block.
 */

private fun markAddWithOverflow(cfg: MutableSbfCFG, addLocInst: LocatedSbfInstruction) {
    // `addInst` is r3 = r3 + r2 in the above example
    val addInst = addLocInst.inst
    check(addInst is SbfInstruction.Bin && addInst.op == BinOp.ADD) {"markAddWithOverflow expects an addition instead of $addInst"}
    val bb = cfg.getMutableBlock(addLocInst.label)
    check(bb != null) {"markAddWithOverflow cannot find block for ${addLocInst.label}"}

    // match assignment (r3 = r4 in the above example)
    val assignLocInst = findDefinitionInterBlock(bb, addInst.dst, addLocInst.pos) ?: return
    val assignInst = assignLocInst.inst
    if (assignInst is SbfInstruction.Bin && assignInst.op == BinOp.MOV && assignLocInst.label == bb.getLabel() /* same block */) {
        val op1 = assignInst.v
        if (op1 !is Value.Reg) {
            return
        }

        val op2 = addInst.v



        val safeMathInst = mutableListOf(addLocInst)
        var (overflowVar, pos) = addInst.dst to addLocInst.pos
        var nextUseLocInst = getNextUseInterBlock(bb, pos+1, overflowVar)

        // match (optionally) r3 = r3 - 1 in the above example
        // Note that we match any instruction r = r + k or r = r - k where k is an immediate value.
        if (nextUseLocInst != null) {
            val nextUseInst = nextUseLocInst.inst
            if (nextUseInst is SbfInstruction.Bin &&
                (nextUseInst.op == BinOp.SUB || nextUseInst.op == BinOp.ADD) &&
                (nextUseInst.v is Value.Imm) &&
                nextUseLocInst.label == bb.getLabel()) {

                overflowVar = nextUseInst.dst
                pos = nextUseLocInst.pos
                safeMathInst.add(nextUseLocInst)
                nextUseLocInst = getNextUseInterBlock(bb, pos+1, overflowVar)
            }
        }

        // match the `select` or the `jump` instruction in the above example
        val selectOrJumpLocInst = nextUseLocInst
        if (selectOrJumpLocInst != null && selectOrJumpLocInst.label == bb.getLabel() /* same block */) {
            when (val selectOrJumpInst = selectOrJumpLocInst.inst) {
                is SbfInstruction.Select -> {
                    if (isAddOverflowCondition(selectOrJumpInst.cond, overflowVar, op1, op2,
                                               bb, assignLocInst.pos, pos, selectOrJumpLocInst.pos)) {
                        safeMathInst.forEach { addSafeMathAnnot(bb, it) }
                        addOverflowAnnot(bb, selectOrJumpLocInst, overflowVar)
                    }
                }
                is  SbfInstruction.Jump.ConditionalJump -> {
                    if (isAddOverflowCondition(selectOrJumpInst.cond, overflowVar, op1, op2,
                                               bb, assignLocInst.pos, pos, selectOrJumpLocInst.pos)) {
                        safeMathInst.forEach { addSafeMathAnnot(bb, it) }
                        addOverflowAnnot(bb, selectOrJumpLocInst, overflowVar)
                    }
                }
                else -> {}
            }
        }
    }
}

/**
 * This function returns true if [cond] does an overflow check:
 *
 * ```
 * z = x + y
 * if (x > z) or (z < x) ...
 * ```
 *
 * ```
 * z = x + y
 * if (y > z) or (z < y) ...
 * ```
 *
 * In addition, we need to make sure that [x], [y], and [z] are not redefined before the overflow condition.
 * [z] cannot be redefined otherwise `isAddOverflowCondition` wouldn't be called.
 * We do check for [x] and [y].
 */
private fun isAddOverflowCondition(cond: Condition, z: Value.Reg, x: Value.Reg, y: Value,
                                   bb: SbfBasicBlock, xPos: Int, yPos: Int, condPos: Int): Boolean {


    fun isNotRedefined(reg: Value.Reg, from:Int) = !isRedefined(bb, reg, from, condPos)
    // We don't use directly equals from Condition because Condition has some other optional parameters
    fun matches(condX: Condition, condY: Condition) =
            (condX.op == condY.op && condX.left == condY.left && condX.right == condY.right)

    return if ((matches(cond, Condition(CondOp.GT, x, z)) ||
                matches(cond, Condition(CondOp.LT, z, x))) &&
               isNotRedefined(x, xPos)) {
        true
    } else {
            y is Value.Reg && (matches(cond, Condition(CondOp.GT, y, z)) ||
                               matches(cond, Condition(CondOp.LT, z, y))) &&
            isNotRedefined(y, yPos)
    }
}


private fun addSafeMathAnnot(bb: MutableSbfBasicBlock, locInst: LocatedSbfInstruction) {
    val inst = locInst.inst
    if (inst is SbfInstruction.Bin && (inst.op == BinOp.ADD || inst.op == BinOp.SUB)) {
        val newMetaData = inst.metaData.plus(Pair(SbfMeta.SAFE_MATH, ""))
        bb.replaceInstruction(locInst.pos, inst.copy(metaData = newMetaData))
    }
}

private fun addOverflowAnnot(bb: MutableSbfBasicBlock, locInst: LocatedSbfInstruction, overflowVar: Value.Reg) {
    when (val inst = locInst.inst) {
        is SbfInstruction.Select -> {
            val newMetaData = inst.metaData
                .plus(
                    Pair(
                        SbfMeta.PROMOTED_OVERFLOW_CHECK,
                        Condition(CondOp.GT, overflowVar, Value.Imm(ULong.MAX_VALUE))
                    )
                )
            bb.replaceInstruction(locInst.pos, inst.copy(metaData = newMetaData))
        }
        is SbfInstruction.Jump.ConditionalJump -> {
            val newMetaData = inst.metaData
                .plus(
                    Pair(
                        SbfMeta.PROMOTED_OVERFLOW_CHECK,
                        Condition(CondOp.GT, overflowVar, Value.Imm(ULong.MAX_VALUE))
                    )
                )
            bb.replaceInstruction(locInst.pos, inst.copy(metaData = newMetaData))

        }
        else -> {}
    }
}
