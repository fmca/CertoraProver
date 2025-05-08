/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY, without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR a PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package report

import analysis.CmdPointer
import datastructures.NonEmptyList
import datastructures.stdcollections.*
import datastructures.toNonEmptyList
import evm.EVM_ADDRESS_SIZE
import kotlinx.serialization.json.*
import log.Logger
import log.LoggerTypes
import log.regression
import report.calltrace.CallTraceAttribute
import report.calltrace.altReprsInTreeView
import report.calltrace.formatter.AlternativeRepresentations
import report.calltrace.formatter.AlternativeRepresentations.Representations
import report.calltrace.formatter.CallTraceValue
import report.calltrace.formatter.CallTraceValueFormatter
import report.calltrace.formatter.FormatterType
import report.calltrace.formatter.FormatterType.Companion.toFormatterType
import report.calltrace.formatter.FormatterType.Companion.toValueFormatterType
import report.calltrace.sarif.Sarif
import report.calltrace.sarif.Sarif.Arg
import rules.ContractInfo
import scene.IClonedContract
import scene.IContractWithSource
import scene.ISceneIdentifiers
import solver.CounterexampleModel
import spec.CVLDefinitionSite
import spec.CVLKeywords
import spec.cvlast.CVLType
import spec.cvlast.typedescriptors.EVMTypeDescriptor
import tac.Tag
import utils.*
import vc.data.CoreTACProgram
import vc.data.TACCmd
import vc.data.TACMeta
import vc.data.TACSymbol
import vc.data.state.TACValue
import java.math.BigInteger

class LocalAssignments(
    private val root: List<Node>,
    /**
     * XXX: kind of a kludge.
     * it would probably be nicer if this didn't own a formatter,
     * and the caller had to pass one instead.
     */
    val formatter: CallTraceValueFormatter,
) {
    sealed class Node : ToJson {
        /** name of the last component of this node, without the entire path */
        abstract val name: String

        class Terminal internal constructor(
            override val name: String,
            val state: State,
            val range: Range?,
        ) : Node() {
            fun formattedValue(formatter: CallTraceValueFormatter): String = this.state.toSarif(formatter).flatten()

            override fun toJson(formatter: CallTraceValueFormatter, fetchId: (Node) -> Int) = buildJsonObject {
                put(CallTraceAttribute.VARIABLE_NAME(), name)

                val sarif = state.toSarif(formatter)
                val value: Arg? = sarif.asArg()

                if (value != null) {
                    put(CallTraceAttribute.VALUE(), value.values.pretty)
                    if (altReprsInTreeView) {
                        putJsonArray(
                            CallTraceAttribute.VALUES(),
                            value.values.asRepList().map(::JsonPrimitive)
                        )
                    }
                    put(
                        CallTraceAttribute.TOOLTIP(),
                        CallTraceValueFormatter.variableTooltip(value.values.pretty)
                    )
                    put(CallTraceAttribute.TRUNCATABLE(), value.truncatable)
                } else {
                    val valueStr = sarif.flatten()
                    Warner.warnOnUnexpectedValue(name, valueStr)
                    put(CallTraceAttribute.VALUE(), valueStr)
                    if (altReprsInTreeView) {
                        putJsonArray(
                            CallTraceAttribute.VALUES(),
                            JsonPrimitive(valueStr)
                        )
                    }
                    put(
                        CallTraceAttribute.TOOLTIP(),
                        CallTraceValueFormatter.variableTooltip(valueStr)
                    )
                    put(CallTraceAttribute.TRUNCATABLE(), false)
                }

                put(CallTraceAttribute.JUMP_TO_DEFINITION(), range as? Range.Range)

                /**
                 * frontend requirements:
                 * 1) terminal nodes _should_ contain the children list property
                 * 2) it should be empty (not null)
                 */
                putJsonArray(CallTraceAttribute.CHILDREN_LIST(), emptyList<JsonElement>())

                put(CallTraceAttribute.UI_ID(), fetchId(this@Terminal))
            }
        }

        internal class NonTerminal(
            override val name: String,
            val children: MutableList<Node>,
        ) : Node() {
            override fun toJson(formatter: CallTraceValueFormatter, fetchId: (Node) -> Int) = buildJsonObject {
                put(CallTraceAttribute.VARIABLE_NAME(), name)
                putJsonArray(
                    CallTraceAttribute.CHILDREN_LIST(),
                    children.map { it.toJson(formatter, fetchId) }
                )
                put(CallTraceAttribute.UI_ID(), fetchId(this@NonTerminal))
            }
        }
    }

    /**
     * An enumeration of the kinds of local assignments that may be displayed in the report.
     * In particular, it is intended to differentiate initialized from uninitialized values, since only the former actually requires formatting.
     * When a variable is initialized after the first failed assert, the SMT may assign it irrelevant value because the formula fails anyway.
     * In such case we want to consider it as [Uninitialized] and report it properly in reports.
     * When a variable is initialized and used in counter example, it is [Initialized] with its expression and type.
     *
     * (the interface is just for grouping)
     *
     * Everything under this interface may be displayed in the Variables Tab of the report.
     */
    sealed interface State {
        val formatterType: FormatterType<*>

        fun toSarif(formatter: CallTraceValueFormatter): Sarif

        object Uninitialized: State {
            override fun toString() = "uninitialized"
            override val formatterType: FormatterType<*>
                get() = FormatterType.Value.Unknown("unknown type (of uninitialized value)") // does this end up being shown??

            override fun toSarif(formatter: CallTraceValueFormatter) =
                CallTraceValueFormatter.unusedValue(formatterType)
        }

        object InitializedButMissing: State {
            override fun toString() = "initialized to unknown"
            override val formatterType: FormatterType<*>
                get() = FormatterType.Value.Unknown("unknown type (of initialized-but-missing value)") // does this end up being shown??

            override fun toSarif(formatter: CallTraceValueFormatter) =
                CallTraceValueFormatter.unknown()
        }

        object ByteMap: State {
            override fun toString() = "bytemap initialized but unknown"
            override val formatterType: FormatterType<*>
                get() = FormatterType.Compound.CVL(CVLType.PureCVLType.DynamicArray.PackedBytes)

            override fun toSarif(formatter: CallTraceValueFormatter) =
                CallTraceValueFormatter.unknown()
        }

        /**
         * Displaying the contents of CVL strings, for that we need the map contents and the length.
         * If the length exceeds [CVLString.MAX_DISPLAYED_LENGTH], we shorten and display `...` at the end.
         *
         * NB: We currently only read the fields from the [contents] map whose indices are multiples of 32.
         * This is not accurate in general, but works in simple cases (and usually we can't afford to run with precise
         * bytemap modeling anyway due to complexity...).
         */
        data class CVLString(
            val contents: TACValue.MappingValue.MapDefinition,
            val length: BigInteger,
        ): State {
            private val errorMsg get() = "(unable to show string contents)"

            override val formatterType: FormatterType<*>
                get() = FormatterType.Compound.CVL(CVLType.PureCVLType.DynamicArray.StringType)

            private val stringRep by lazy {
                length.toIntOrNull()?.let { lengthInt ->
                    val (displayLength, truncating) = if (lengthInt <= MAX_DISPLAYED_LENGTH) {
                        lengthInt to false
                    } else {
                        MAX_DISPLAYED_LENGTH to true
                    }

                    var wholeStringAsBytes = "".toByteArray(Charsets.UTF_8)

                    for (i in (0 until displayLength).step(32)) {
                        val readVal =
                            contents[listOf(TACValue.valueOf(i))]
                                .asBigIntOrNull() ?: return@lazy null

                        val readValBytes = readVal.toByteArray()
                        if (readValBytes.size > 32) {
                            return@lazy null
                        }

                        val readValBytesPaddedLeft = ByteArray(32 - readValBytes.size) + readValBytes

                        val readValTruncatedRight = if (lengthInt < i + 32) {
                            val bytesToKeep = (lengthInt % 32) // * 8
                            readValBytesPaddedLeft.copyOfRange(0, bytesToKeep)
                        } else {
                            readValBytesPaddedLeft
                        }
                        wholeStringAsBytes += readValTruncatedRight
                    }
                    val (string, utf8Succeeded) =
                        @Suppress("SwallowedException")
                        try {
                            // decodeToString doesn't need charset specified, just does utf8
                            wholeStringAsBytes.decodeToString(throwOnInvalidSequence = true) to true
                        } catch (_: CharacterCodingException) {
                            "(invalid UTF-8)" to false
                        }
                    val postfix = ite(truncating && utf8Succeeded, "...", "")
                    string + postfix
                }
            }

            override fun toSarif(formatter: CallTraceValueFormatter) =
                (
                        stringRep?.let { strRep ->
                            Arg(
                                AlternativeRepresentations.RepresentationsMap(Representations.Pretty to strRep),
                                "CVL string",
                                type = formatterType.toTypeString(),
                                truncatable = false,
                            )
                        } ?: CallTraceValueFormatter.unknownArg()
                        ).asSarif

            override fun toString(): String = stringRep ?: errorMsg

            companion object {
                /** The maximum number of bytes to display in full for a given cvl string. */
                const val MAX_DISPLAYED_LENGTH = 10 * 32
            }
        }

        data class Initialized(val value: TACValue, val type: CVLType.PureCVLType?): State {
            override fun toString() = "initialized"
            override fun toSarif(formatter: CallTraceValueFormatter) =
                CallTraceValue.cvlCtfValueOrUnknown(value, type).toSarif(formatter, "initial value")

            override val formatterType: FormatterType<*>
                get() = type?.toFormatterType() ?: FormatterType.Value.Unknown("unknown type (initialized value)") // xxx
        }

        data class Contract(val value: TACValue.PrimitiveValue.Integer, val info: ContractInfo) : State {
            override fun toString() = "contract ${info.name} with instance ${info.instanceId}"
            override fun toSarif(formatter: CallTraceValueFormatter): Sarif =
                formatter.valueToSarif(
                    value,
                    // not declaring this as address here, since this is the one case where we want the value to be
                    // formatted as a number
                    EVMTypeDescriptor.UIntK(EVM_ADDRESS_SIZE).toValueFormatterType(),
                    "contract address"
                ).let { sarif ->
                    /** "special solution" to do what we'd normally do for addresses in the call trace value formatting:
                     *    addresses don't switch to decimal representation, but show hex in DEC mode
                     *  not the prettiest solution, but rather local, and should do for the time being */
                    sarif.asArg()?.let { arg ->
                        val new = arg.values.toMutableMap()
                        runIf (new.size == Representations.entries.size) {
                            new[Representations.Decimal] = new[Representations.Hex]!!
                            arg.copy(values = AlternativeRepresentations.RepresentationsMap(new)).asSarif
                        }
                    } ?: sarif
                }

            override val formatterType: FormatterType<*>
                get() = EVMTypeDescriptor.address.toValueFormatterType()
        }
    }

    fun toJson(): List<JsonObject> {
        val ordering = this.uiIdOrdering()
        fun fetchId(node: Node): Int = ordering[node] ?: error("internal error: uiId already computed for all nodes")

        return this.root.map { it.toJson(formatter, ::fetchId) }
    }

    /** currently, this is a level-order traversal */
    private fun uiIdOrdering(): Map<Node, Int> {
        var uiId = 1
        val nodeToId: MutableMap<Node, Int>  = mutableMapOf()

        val queue: ArrayDeque<Node> = ArrayDeque(this.root)

        while (!queue.isEmpty()) {
            val node = queue.removeFirst()

            nodeToId[node] = uiId
            uiId += 1

            if (node is Node.NonTerminal) {
                queue.addAll(node.children)
            }
        }

        return nodeToId
    }

    /**
     * a flat list of only [Node.Terminal]s, with fully-qualified names.
     * e.g. a chain of the form `foo -> bar -> baz`, where `foo` and `bar` are non-terminals,
     * will become a single terminal with the name "foo.bar.baz", and the data of `baz`.
     *
     * this exists for legacy code: we used to output only terminals,
     * with fully-qualified names as described above.
     */
    val flattenedTerminals: List<Node.Terminal> by lazy {
        val terminals: MutableList<Node.Terminal> = mutableListOf()

        fun recurse(node: Node, prefix: String?) {
            when (node) {
                is Node.NonTerminal -> {
                    for (child in node.children) {
                        recurse(
                            node = child,
                            prefix = prefix?.appendComponent(node.name) ?: node.name
                        )
                    }
                }
                is Node.Terminal -> {
                    val terminal = Node.Terminal(
                        name = prefix?.appendComponent(node.name) ?: node.name,
                        state = node.state,
                        range = node.range,
                    )
                    terminals.add(terminal)
                }
            }
        }

        for (node in this.root) {
            recurse(node, prefix = null)
        }

        terminals
    }

    fun terminalsByName(): Map<String, Node.Terminal> = this.flattenedTerminals.associateBy { it.name }

    val size: Int = this.flattenedTerminals.size

    /** a kludge to maintain compatibility with existing tests */
    internal fun logForTests() {
        Logger.regression {
            val assignmentsExceptContracts = this
                .flattenedTerminals
                .filter { it.state !is State.Contract }
                .map { it.name }
                .sorted()

            "The names of the local variables are $assignmentsExceptContracts"
        }
    }
}

fun LocalAssignments(
    model: CounterexampleModel,
    program: CoreTACProgram,
    modelValueToContract: Map<TACValue.PrimitiveValue.Integer, ContractInfo>,
    formatter: CallTraceValueFormatter,
    scene: ISceneIdentifiers,
): LocalAssignments {
    val root: MutableList<LocalAssignments.Node> = mutableListOf()

    fun push(path: NamePath, state: LocalAssignments.State, range: Range?) {
        // find insertion point
        var scope = root
        path
            .components
            .allButLast()
            .forEach { component ->
                /** this assumes names per scope are unique, which we validate elsewhere */
                val existingNode = scope.find { it.name == component }

                scope = when (existingNode) {
                    is LocalAssignments.Node.NonTerminal -> existingNode.children

                    is LocalAssignments.Node.Terminal -> {
                        /**
                         * this shouldn't be possible, since any [NamePath.nonClassMemberProperties]
                         * have already been concatenated at this point.
                         */
                        error("internal error: more components in name path, but reached terminal")
                    }

                    null -> {
                        val node = LocalAssignments.Node.NonTerminal(
                            name = component,
                            children = mutableListOf(),
                        )
                        scope.add(node)
                        node.children
                    }
                }
            }

        val node = LocalAssignments.Node.Terminal(
            name = path.components.last(),
            state,
            range,
        )

        scope.add(node)
    }

    val (displayNameToLength, displayNameToContents) = collectCVLStringsSymbols(model.tacAssignments.keys)

    val (cvlVarsBeforeAssert, cvlVarsAfterAssert) = beforeAndAfterAssert(program, model)

    for (tv in cvlVarsAfterAssert) {
        push(
            NamePath.fromVar(tv),
            LocalAssignments.State.Uninitialized, // variables that were initialized after the failed assert contain junk values.
            tv.meta[TACMeta.CVL_DEF_SITE]?.range,
        )
    }

    for (tv in cvlVarsBeforeAssert) {
        val modelValue = model.valueAsTACValue(tv)
        val varType = tv.meta[TACMeta.CVL_TYPE]
        val displayName = tv.meta[TACMeta.CVL_DISPLAY_NAME]

        val state = when {
            displayNameToContents[displayName] == tv -> {
                checkWarn(tv.tag == Tag.ByteMap)
                { "unexpected case when trying to show CVL string \"$tv\": not a bytemap" }
                checkWarn(varType is CVLType.PureCVLType.DynamicArray.StringType)
                { "unexpected case when trying to show CVL string \"$tv\": not a CVL string type" }
                checkWarn(modelValue is TACValue.MappingValue.MapDefinition)
                { "unexpected case when trying to show CVL string \"$tv\": TACValue is not a map definition, got: \"$modelValue\"" }

                (modelValue as? TACValue.MappingValue.MapDefinition)?.let { mapContents ->
                    displayNameToLength[displayName]?.let { lengthSym ->
                        (model.valueAsTACValue(lengthSym) as? TACValue.PrimitiveValue)?.asBigInt?.let { lengthModelValue ->
                            LocalAssignments.State.CVLString(mapContents, lengthModelValue)
                        }
                    }
                } ?: LocalAssignments.State.ByteMap
            }

            tv.tag == Tag.ByteMap ->
                LocalAssignments.State.ByteMap

            modelValue != null -> {
                LocalAssignments.State.Initialized(modelValue, varType)
            }

            else -> {
                Logger(LoggerTypes.REPORT_UTILS).info { "Variable $tv is not in the model." }
                LocalAssignments.State.InitializedButMissing
            }
        }

        push(NamePath.fromVar(tv), state, tv.meta[TACMeta.CVL_DEF_SITE]?.range)
    }

    for ((modelValue, info) in modelValueToContract) {
        val contract = info.resolve(scene)
        val range = when (contract) {
            is IContractWithSource -> contract.src.sourceSegment()?.range
            is IClonedContract -> (scene.getContract(contract.sourceContractId) as? IContractWithSource)?.src?.sourceSegment()?.range
            else -> null
        }

        // contract values are all terminals.
        // no point in attempting to handle structs here.
        val node = LocalAssignments.Node.Terminal(
            name = info.name,
            state = LocalAssignments.State.Contract(modelValue, info),
            range,
        )
        root.add(node)
    }

    return LocalAssignments(root, formatter)
}

private class NamePath private constructor(val components: NonEmptyList<String>) {
    companion object {
        private fun splitComponents(name: String): NonEmptyList<String> {
            @Suppress("ForbiddenMethodCall")
            val split = name.split('.')

            return split.toNonEmptyList() ?: error("unreachable. split can't return empty lists")
        }

        private val nonClassMemberProperties = setOf(
            "length",
        )

        /** this can use [TACMeta.CVL_STRUCT_PATH] but the complexity is questionable */
        fun fromVar(tv: TACSymbol.Var): NamePath {
            val split = splitComponents(tv.name())
            val last = split.last()

            val components = if (last !in nonClassMemberProperties) {
                split
            } else {
                // concatenate last access to the one before it,
                // since it's a "special" property.
                //
                // I didn't check, but I think these properties are not reserved words,
                // and so we can have an identifier that is just this property and nothing else?
                val newTail = run {
                    val tail = split.takeLast(2)

                    if (tail.size == 2) {
                        tail[0].appendComponent(tail[1])
                    } else {
                        tail[0]
                    }
                }

                split
                    .dropLast(2)
                    .plus(newTail)
                    .toNonEmptyList()!!
            }

            return NamePath(components)
        }
    }
}

private object Warner {
    private var alreadyWarned = false

    fun warnOnUnexpectedValue(name: String, valueStr: String) {
        if (!alreadyWarned) {
            // not really expecting this to happen -- let's monitor ..
            Logger(LoggerTypes.COMMON).warn {
                "unexpected display value in variables tab (variable: $name, displayValue: $valueStr)"
            }
            alreadyWarned = true
        }
    }
}

private fun TACSymbol.Var.name() = this.meta[TACMeta.CVL_DISPLAY_NAME] ?: this.namePrefix

private fun beforeAndAfterAssert(tacObject: CoreTACProgram, model: CounterexampleModel): Pair<Set<TACSymbol.Var>, Set<TACSymbol.Var>> {
    val beforeAssert = mutableSetOf<TACSymbol.Var>()
    val afterAssert = mutableSetOf<TACSymbol.Var>()
    var currSet = beforeAssert

    val topoSortedBlocks = tacObject.topoSortFw.filter { nbId -> nbId in model.reachableNBIds }
    require(topoSortedBlocks.isNotEmpty()) {
        "In ${tacObject.name}, expected a non-empty list of blocks reachable in the counter-example model"
    }

    val graph = tacObject.analysisCache.graph

    for (lcmd in graph.iterateFrom(CmdPointer(topoSortedBlocks.first(), 0), topoSortedBlocks)) {
        when (val stmt = lcmd.cmd) {
            is TACCmd.Simple.AssertCmd -> {
                if (stmt.isViolated(model)) {
                    currSet = afterAssert
                }
            }

            is TACCmd.Simple.AssigningCmd -> {
                val lhs = stmt.lhs

                if (lhs.meta[TACMeta.CVL_DEF_SITE] is CVLDefinitionSite.Rule && CVLKeywords.find(lhs.name()) == null) {
                    currSet.add(lhs)
                }
            }

            else -> { }
        }
    }

    /**
     * the solver's model may contain "duplicates",
     * for reasons I'm not going to try and figure out right now.
     * and this may be completely sound, but we don't want these in the output.
     * as a dirty fix, we de-duplicate them here,
     * keeping only the most recent assignments which have the same name.
     *
     * impl notes:
     * 1) an optimization (if feasible), is to do this while building these sets,
     *    instead of in this separate pass.
     * 2) we iterate backwards because we want to keep the most recent assignment.
     * 3) Kotlin sets are ordered - iteration order is by insertion order,
     *    however *we convert to lists before merging*.
     *    otherwise, relative order may not be maintained (probably because it's re-hashing?)
     * 4) if the [TACMeta.CVL_DISPLAY_NAME] is null, then we default to a unique name,
     *    so the variable is always kept if this meta is missing.
     */
    val keep = beforeAssert
        .toList()
        .plus(afterAssert.toList())
        .reversed()
        .distinctBy(TACSymbol.Var::name)
        .toSet()

    beforeAssert.removeIf { !keep.contains(it) }
    afterAssert.removeIf { !keep.contains(it) }

    return beforeAssert to afterAssert
}

private sealed interface ToJson {
    fun toJson(
        formatter: CallTraceValueFormatter,
        fetchId: (LocalAssignments.Node) -> Int,
    ): JsonObject
}

private fun String.appendComponent(component: String) = "$this.$component"