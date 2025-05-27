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

package verifier.equivalence

import analysis.*
import datastructures.stdcollections.*
import evm.DEFAULT_SIGHASH_SIZE
import kotlin.streams.toList
import verifier.equivalence.tracing.BufferTraceInstrumentation
import log.*
import report.calltrace.CallInputsAndOutputs
import report.calltrace.calldataMovement
import report.calltrace.formatter.CallTraceValue
import report.calltrace.formatter.CallTraceValueFormatter
import report.calltrace.formatter.LayoutDecoderStrategy
import report.calltrace.registerCalldataMovement
import rules.RuleCheckResult
import scene.ContractClass
import scene.TACMethod
import solver.CounterexampleModel
import tac.CallId
import utils.*
import vc.data.*
import verifier.equivalence.CEXUtils.withFailureString
import verifier.equivalence.EquivalenceChecker.Companion.pp
import verifier.equivalence.EquivalenceChecker.Companion.toList
import verifier.equivalence.StaticBufferRefinement.fmtError
import java.math.BigInteger
import java.util.stream.Collectors

private val logger = Logger(LoggerTypes.EQUIVALENCE)

/**
 * Called to analyze/refine/explain counter examples generated during the process.
 *
 * [ruleResult] is used to report a failure if no refinement is possible. The counterexample
 * was found in [vcProgram] and its values are found in [theModel]. The cex was found using the instrumentation
 * in [methodAContext] and [methodBContext]; the overall comparison is happening in [context]. [instLevels] describes
 * the traces being explored, and [pairwiseProofManager] is used to register refinements if necessary.
 */
internal class CounterExampleAnalyzer(
    private val ruleResult: RuleCheckResult,
    private val theModel: CounterexampleModel,
    private val vcProgram: CoreTACProgram,
    private val methodAContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
    private val methodBContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>,
    private val instLevels: EquivalenceChecker.IInstrumentationLevels,
    override val context: QueryContext,
    val pairwiseProofManager: EquivalenceChecker.PairwiseProofManager
) : WithQueryContext {

    fun interface CEXContinuation {
        suspend fun resume(): EquivalenceChecker.SatInterpretation
    }

    /**
     * Really a specialized version of the [Either] type to make type signatures easier to read
     */
    private sealed interface MatchingEventData<out T> {
        data class Found<T>(val what: T) : MatchingEventData<T>
        data object Missing : MatchingEventData<Nothing>
    }

    /**
     * Representation of selecting a value at [loc] out of [base].
     */
    private data class Sel(
        val base: TACSymbol.Var,
        val loc: TACExpr
    )

    private val selectorMatch = PatternMatcher.Pattern.AssigningPattern0(
        klass = TACCmd.Simple.AssigningCmd.AssignExpCmd::class.java,
        extract = ext@{ _, cmd ->
            val r = cmd.rhs as? TACExpr.Select ?: return@ext PatternMatcher.ConstLattice.NoMatch
            val baseSym = (r.base as? TACExpr.Sym.Var)?.s ?: return@ext PatternMatcher.ConstLattice.NoMatch
            PatternMatcher.ConstLattice.Match(
                Sel(
                    base = baseSym,
                    loc = r.loc
                )
            )
        }
    )

    private val selectEqualityMatch = PatternDSL.build {
        (selectorMatch.asBuildable() `==` selectorMatch.asBuildable()).withAction { where, o1, o2 ->
            Triple(where, o1, o2)
        }
    }

    /**
     * Strip skey applications off of expressions
     */
    private fun stripSkey(e: TACExpr) : TACSymbol? {
        return when(e) {
            is TACExpr.Sym -> e.s
            is TACExpr.Apply -> {
                if(e.f != TACBuiltInFunction.ToStorageKey.toTACFunctionSym() || e.ops.size != 1) {
                    return null
                }

                return stripSkey(e.ops[0])
            }
            else -> null
        }
    }

    private fun explainStorageDifference(
        failingAssert: LTACCmdView<TACCmd.Simple.AssertCmd>,
    ) : Either<EquivalenceChecker.MismatchExplanation.StorageExplanation, String> {
        fun fail() : Either<Nothing, String> {
            return "Couldn't explain storage difference".toRight()
        }
        val sym = failingAssert.cmd.o as? TACSymbol.Var ?: return fail()
        val comp = PatternMatcher.compilePattern(vcProgram.analysisCache.graph, selectEqualityMatch)
        val (where, o1, o2) = comp.query(sym, failingAssert.wrapped).toNullableResult() ?: return fail()
        val eq = vcProgram.analysisCache.graph.elab(where.ptr).maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()?.cmd?.rhs?.let {
            it as? TACExpr.BinRel.Eq
        } ?: return fail()

        val srcContract1 = o1.base.meta.get(TACMeta.STORAGE_KEY) ?: return fail()
        val srcContract2 = o2.base.meta.get(TACMeta.STORAGE_KEY) ?: return fail()
        val loc = stripSkey(o1.loc) ?: return fail()
        val idx = theModel.valueAsBigInteger(loc).leftOr {
            return fail()
        }
        val s1Val = theModel.evalExprByRhs(eq.o1).takeIf {
            it.first && it.second != null
        } ?: return fail()
        val s2Val = theModel.evalExprByRhs(eq.o2).takeIf {
            it.first && it.second != null
        } ?: return fail()
        return EquivalenceChecker.MismatchExplanation.StorageExplanation(
            slot = idx,
            leftOp = EquivalenceChecker.MismatchExplanation.StorageExplanation.StorageRepr(
                which = scene.getContract(srcContract1) as ContractClass,
                slotValue = s1Val.second!!
            ),
            rightOp = EquivalenceChecker.MismatchExplanation.StorageExplanation.StorageRepr(
                which = scene.getContract(srcContract2) as ContractClass,
                slotValue = s2Val.second!!
            )
        ).toLeft()
    }

    /**
     * From the [BufferTraceInstrumentation.CallEvent] object
     * found at [where] in [graph], extract the [verifier.equivalence.EquivalenceChecker.ExternalCall] object
     * describing the call, using the values in [model]. [maxOrd] indicates we are only interested in calls up to that index,
     * if the ordinal of [ce] is greater or equal to this parameter, this function returns null. Otherwise, it returns the extracted
     * ordinal and the [verifier.equivalence.EquivalenceChecker.ExternalCall] object.
     */
    private fun extractEnvironment(
        graph: TACCommandGraph,
        where: LTACCmd,
        ce: BufferTraceInstrumentation.CallEvent,
        model: CounterexampleModel,
        maxOrd: Int?
    ) : Pair<Int, EquivalenceChecker.ExternalCall>? {
        val ord = model.valueAsBigInteger(ce.ordinal).leftOrNull()?.intValueExact() ?: return run {
            logger.warn {
                "Can't even resolve ordinal symbol at $where in $ce"
            }
            null
        }
        // save processing, if we don't want this, don't make it
        if(maxOrd != null && ord >= maxOrd) {
            return null
        }
        return ord to callEventDataToInteraction(where, ce, model, graph).toValue({ it }, {
            EquivalenceChecker.ExternalCall.Incomplete(
                it
            )
        })
    }

    /**
     * Try to extract the [verifier.equivalence.EquivalenceChecker.ExternalCall.Complete]
     * from the [BufferTraceInstrumentation.CallEvent] [ce]
     * found at [where] in [graph] using the values in [model].
     */
    private fun callEventDataToInteraction(
        where: LTACCmd,
        ce: BufferTraceInstrumentation.CallEvent,
        model: CounterexampleModel,
        graph: TACCommandGraph
    ): Either<EquivalenceChecker.ExternalCall.Complete, String> {
        fun <T> Either<T, CounterexampleModel.ResolvingFailure>.withFailureString(what: () -> String) =
            this.mapRight {
                "Failed resolving ${what()} @ $where with $ce: $it"
            }

        fun <T, U> Either<T, CounterexampleModel.ResolvingFailure>.formatErrorOrBind(
            what: String,
            f: (T) -> Either<U, String>
        ): Either<U, String> {
            return when (this) {
                is Either.Left -> f(this.d)
                is Either.Right -> "Failed resolving calldata at $where: couldn't get value for $what; ${this.d}".toRight()
            }
        }

        val callee = model.valueAsBigInteger(ce.callee).withFailureString { "callee address" }.leftOr { return it }
        val returnSize =
            model.valueAsBigInteger(ce.returnDataSize).withFailureString { "return address" }.leftOr { return it }
        val returnResult = model.valueAsBigInteger(ce.returnCode).withFailureString { "return code" }.leftOr { return it } != BigInteger.ZERO
        val calleeCodesize =
            model.valueAsBigInteger(ce.calleeCodeSize).withFailureString { "callee codesize" }.leftOr { return it }
        val value = model.valueAsBigInteger(ce.value).withFailureString { "sent value" }.leftOr { return it }
        val calldata = model.valueAsBigInteger(ce.bufferLength).formatErrorOrBind("input buffer length") { buffLength ->
            model.valueAsBigInteger(ce.bufferStart).formatErrorOrBind("input buffer offset") { buffStart ->
                PreciseBufferExtraction.extractBufferModel(
                    start = buffStart,
                    where = where.ptr,
                    graph = graph,
                    model = model,
                    buffer = ce.memoryCapture,
                    len = buffLength
                ).toList(buffLength)
            }
        }
        return EquivalenceChecker.ExternalCall.Complete(
            returnSize = returnSize,
            callee = callee,
            callResult = returnResult,
            calleeCodesize = calleeCodesize,
            calldata = calldata,
            value = value
        ).toLeft()
    }

    /**
     * Find all calls in the inlined method body with [callId], up to [maxOrd] if it is non-null.
     * Returns a list of discovered [verifier.equivalence.EquivalenceChecker.ExternalCall], which
     * may or may not include all of the requested events.
     */
    private fun getCallsBefore(
        callId: CallId,
        maxOrd: Int?
    ) : List<EquivalenceChecker.ExternalCall> {
        val trace = vcProgram.parallelLtacStream().mapNotNull {
            it `to?` it.maybeAnnotation(BufferTraceInstrumentation.CallEvent.META_KEY)
        }.filter { (where, _) ->
            where.ptr.block.calleeIdx == callId && where.ptr.block in theModel.reachableNBIds
        }.mapNotNull { (where, ce) ->
            extractEnvironment(
                graph = vcProgram.analysisCache.graph,
                model = theModel,
                where = where,
                ce = ce,
                maxOrd = maxOrd
            )
        }.collect(Collectors.toMap({ it.first }, { it.second }))
        val toRet = mutableListOf<EquivalenceChecker.ExternalCall>()
        for(i in 0 until (maxOrd ?: trace.takeIf { it.isNotEmpty() }?.keys?.max() ?: 0)) {
            toRet.add(
                trace[i] ?: EquivalenceChecker.ExternalCall.Incomplete("Could not find information on call number $i")
            )
        }
        return toRet
    }

    /**
     * Extract the [CallTraceValue] representation of arguments
     * from the [CallInputsAndOutputs] that were found the body of [method].
     */
    private fun extractArguments(
        method: EquivalenceChecker.InlinedInstrumentation<*>,
        cio: CallInputsAndOutputs,
        model: CounterexampleModel
    ) : Map<Int, CallTraceValue> {
        return cio.externalCall(method.methodCallId)?.let { aArgs ->
            val m = aArgs.calldataFamily.toValueMap(
                model, DEFAULT_SIGHASH_SIZE
            )
            LayoutDecoderStrategy(
                names = aArgs.extra.paramNames,
                paramTypes = aArgs.extra.paramTypes,
                byteOffsetToModelValue = m
            ).asMap()
        }.orEmpty()
    }

    /**
     * Get a "friendly" explanation of the input in the case of a CEX.
     *
     * This includes the calldata arguments, some environment information etc.
     */
    private fun getInputExplanation() : EquivalenceChecker.InputExplanation {
        val model = theModel
        val ruleProg = vcProgram
        val env = RuleGenerator.extractEnvironmentValues(
            model, ruleProg
        )
        val msgVal = env[EthereumVariables.callvalue]
        val caller = env[EthereumVariables.caller]
        val cio = CallInputsAndOutputs(
            blocks = ruleProg.topoSortFw.filter {
                it in model.reachableNBIds
            },
            model = model,
            scene = scene,
            analysisCache = ruleProg.analysisCache
        )
        val ctf = CallTraceValueFormatter(
            model = model,
            scene = scene,
            addrToContract = mapOf()
        )
        val methodACallId = methodAContext.methodCallId
        val methodBCallId = methodBContext.methodCallId
        ruleProg.parallelLtacStream().filter {
            it.ptr.block.calleeIdx == methodACallId || it.ptr.block.calleeIdx == methodBCallId
        }.mapNotNull {
            it.maybeNarrow<TACCmd.Simple.AssigningCmd.AssignExpCmd>()
        }.flatMap {
            val callIdx = it.ptr.block.calleeIdx
            it.cmd.calldataMovement(model, callIdx).stream().map {
                it to callIdx
            }
        }.sequential().forEach { (mov, id) ->
            cio.registerCalldataMovement(mov, id)
        }
        val methodAArgs = extractArguments(methodAContext, cio, model)
        val methodBArgs = extractArguments(methodBContext, cio, model)
        val argOrds = methodAArgs.keys + methodBArgs.keys
        val args = mutableListOf<EquivalenceChecker.Argument>()
        for(i in argOrds.sorted()) {
            val aArg = methodAArgs[i]
            val bArg = methodBArgs[i]
            val aStringRepr = aArg?.toSarif(ctf, tooltip = "")?.flatten()
            val bStringRepr = bArg?.toSarif(ctf, tooltip = "")?.flatten()
            val argFormat = aStringRepr?.let {
                if(bStringRepr != null && bStringRepr != it) {
                    logger.warn {
                        "Conflicting argument representations for $i ${aArg.paramName} ${bArg.paramName}: $aStringRepr vs $bStringRepr"
                    }
                    "$aStringRepr / $bStringRepr"
                } else {
                    it
                }
            } ?: bStringRepr ?: "<no value found>"
            val (argName, altName) = if(aArg?.paramName != null) {
                aArg.paramName to bArg?.paramName
            } else {
                bArg?.paramName to null
            }
            if(argName == null) {
                continue
            }
            args.add(
                EquivalenceChecker.Argument(
                    ordinal = i,
                    name = argName,
                    value = argFormat,
                    altName = altName
                )
            )
        }
        return EquivalenceChecker.InputExplanation(
            argumentFormatting = args,
            messageValue = msgVal,
            sender = caller
        )
    }

    /**
     * Given a mismatch at index [eventIndex], find the [verifier.equivalence.EquivalenceChecker.LTraceEventMarker]
     * describing the event for which there was a mismatch. This might not be found, if one method has an external
     * event and the other does not.
     */
    private fun <T: EquivalenceChecker.METHOD_MARKER> extractEventData(
        context: EquivalenceChecker.InlinedInstrumentation<T>,
        vcProgram: CoreTACProgram,
        theModel: CounterexampleModel,
        eventIndex: BigInteger
    ) : MatchingEventData<EquivalenceChecker.LTraceEventMarker<T>> {
        return vcProgram.parallelLtacStream().filter {
            it.ptr.block.calleeIdx == context.methodCallId && it.ptr.block in theModel.reachableNBIds
        }.mapNotNull {
            it `to?` it.maybeAnnotation(BufferTraceInstrumentation.TraceIndexMarker.META_KEY)
        }.filter { (_, eventInfo) ->
            theModel.valueAsBigInteger(eventInfo.indexVar).leftOrNull() == eventIndex
        }.toList().singleOrNull()?.let { (vcWhere, eventInfo) ->
            val origSite = context.instrumentation.useSiteInfo.keysMatching { _, info ->
                info.id == eventInfo.id
            }.single()
            MatchingEventData.Found(
                EquivalenceChecker.LTraceEventMarker(
                    origProgramSite = origSite,
                    vcProgramSite = vcWhere.ptr,
                    marker = eventInfo
                )
            )
        } ?: MatchingEventData.Missing
    }

    /**
     * Called as the continuation if the [TraceMinimizer] couldn't find an ealier mismatch. Start refinment, if possible
     */
    private suspend fun postMinimizationAnalysis(
        eventIdx: BigInteger,
    ) : EquivalenceChecker.SatInterpretation {
        val methodAEvent = extractEventData(
            methodAContext,
            vcProgram,
            theModel,
            eventIdx
        )
        val methodBEvent = extractEventData(
            methodBContext,
            vcProgram,
            theModel,
            eventIdx
        )
        if(methodAEvent is MatchingEventData.Missing && methodBEvent is MatchingEventData.Missing) {
            return EquivalenceChecker.SatInterpretation.GaveUp("Both event information is missing", ruleResult)
        }

        /*
         * Let's try to refine counter examples first
         */
        val aOverride = MemoryImprecisionAnalyzer.analyze(
            theModel,
            vcProgram,
            methodAContext
        )
        val bOverride = MemoryImprecisionAnalyzer.analyze(
            theModel,
            vcProgram,
            methodBContext
        )
        logger.debug {
            "CEX analysis yielded: $aOverride and $bOverride"
        }
        val aSucc = aOverride?.let { (where, depth) ->
            pairwiseProofManager.registerALoadOverride(where, depth)
        } == true
        val bSucc = bOverride?.let { (where, depth) ->
            pairwiseProofManager.registerBLoadOverride(where, depth)
        } == true
        // retry with more precision
        if(aSucc || bSucc) {
            return EquivalenceChecker.SatInterpretation.Refine(
                Explorer(
                    traceLevel = instLevels,
                    context = context
                )
            )
        }
        // this means we have a log/call in one method but not the other
        if(methodAEvent is MatchingEventData.Missing || methodBEvent is MatchingEventData.Missing) {
            check(instLevels.traceLevel != BufferTraceInstrumentation.TraceTargets.Results)
            return tryMissingInterpretation(
                eventIdx, methodAEvent, methodAContext, methodBEvent, methodBContext
            )
        }
        val aDiff = (methodAEvent as MatchingEventData.Found).what
        val bDiff = (methodBEvent as MatchingEventData.Found).what

        /**
         * Did the buffer hashes differ in the mismatch?
         */
        val bufferHashDiffers = theModel.valueAsBigInteger(aDiff.marker.bufferHash).leftOrNull()?.let { aHash ->
            theModel.valueAsBigInteger(bDiff.marker.bufferHash).leftOrNull()?.let { bHash ->
                aHash == bHash
            }
        } == false
        if(bufferHashDiffers) {
            /**
             * If so, was this legit?
             */
            val aBufferDataE = tryExtractBufferModel(aDiff)
            val bBufferDataE = tryExtractBufferModel(bDiff)
            val exactBuffersSame = aBufferDataE.bindLeft { aBuffer ->
                bBufferDataE.mapLeft { bBuffer ->
                    aBuffer == bBuffer
                }
            }.leftOrNull() == true
            /**
             * If not, see if we can prove they are always equal using [StaticBufferRefinement]. If this fails,
             * goto [explainCounterExample]
             */
            if(exactBuffersSame) {
                StaticBufferRefinement.tryRefineBuffers(
                    aTraceAndContext = EquivalenceChecker.LTraceWithContext(
                        trace = aDiff,
                        context = methodAContext,
                        eventIndex = eventIdx
                    ),
                    bTraceAndContext = EquivalenceChecker.LTraceWithContext(
                        trace = bDiff,
                        context = methodBContext,
                        eventIndex = eventIdx
                    ),
                    scene = scene,
                    targetEvents = instLevels.traceLevel
                )?.let { (aRefine, bRefine) ->
                    /**
                     * We aren't done just because the extraction works, we need to prove the contents equal;
                     * use the solver
                     */
                    val ref = StaticBufferEquality(
                        siteA = aDiff.origProgramSite,
                        siteB = bDiff.origProgramSite,
                        parent = instLevels,
                        refineA = aRefine,
                        refineB = bRefine,
                        context = context
                    ) {
                        /**
                         * Couldn't actually resolve, never mind, keep analyzing the CEX
                         */
                        explainCounterExample(
                            aDiff, bDiff
                        )
                    }
                    return EquivalenceChecker.SatInterpretation.Refine(ref)
                }
            }
        }
        /**
         * No refinement attempted, go directly to [explainCounterExample]
         */
        return explainCounterExample(aDiff, bDiff)
    }

    /**
     * Called when we are sure there is a CEX and mismatch.
     */
    private fun explainCounterExample(
        aDiff: EquivalenceChecker.LTraceEventMarker<EquivalenceChecker.METHODA>,
        bDiff: EquivalenceChecker.LTraceEventMarker<EquivalenceChecker.METHODB>
    ) : EquivalenceChecker.SatInterpretation {
        val aEvent = traceMarkerToEvent(aDiff).leftOr {
            return EquivalenceChecker.SatInterpretation.GaveUp(
                "Failed extracting explanation from ${methodA.pp()}: ${it.right()}",
                ruleResult
            )
        }
        val bEvent = traceMarkerToEvent(bDiff).leftOr {
            return EquivalenceChecker.SatInterpretation.GaveUp(
                "Failed extracting explanation from ${methodB.pp()}: ${it.right()}",
                ruleResult
            )
        }
        val priorCalls = theModel.valueAsBigInteger(
            aDiff.marker.numCalls
        ).leftOrNull()?.intValueExact()?.let { priorCalls ->
            getCallsBefore(methodAContext.methodCallId, priorCalls)
        }

        return EquivalenceChecker.SatInterpretation.RealCounterExample(
            inputExplanation = getInputExplanation(),
            priorEvents = priorCalls,
            diffExplanation = EquivalenceChecker.MismatchExplanation.DifferentEvents(
                eventInA = aEvent,
                eventInB = bEvent
            ),
            ruleCheckResult = ruleResult
        )
    }

    /**
     * A single analysis that is split into three parts, allowing calling back out to solver at most 2 extra times.
     * This is the public entry point, which first tries to figure out what fails, and the minimize.
     */
    suspend fun analyzeCounterExample() : EquivalenceChecker.SatInterpretation {
        val failingAssertOpt = vcProgram.parallelLtacStream().mapNotNull {
            it.maybeNarrow<TACCmd.Simple.AssertCmd>()
        }.filter {
            EquivalenceChecker.STORAGE_EQUIVALENCE_ASSERTION in it.cmd.meta || EquivalenceChecker.TRACE_EQUIVALENCE_ASSERTION in it.cmd.meta
        }.filter {
            theModel.valueAsBoolean(it.cmd.o).leftOrNull() == false
        }.findFirst()
        if (failingAssertOpt.isEmpty) {
            return EquivalenceChecker.SatInterpretation.GaveUp(
                "Couldn't find failing assertion in counterexample",
                ruleResult
            )
        }
        val failingAssert = failingAssertOpt.get()
        /**
         * If this was a failing assertion of storage equivalence, there is nothing more to do, explain the difference
         * and return
         */
        if (EquivalenceChecker.STORAGE_EQUIVALENCE_ASSERTION in failingAssert.cmd.meta) {
            return explainStorageDifference(failingAssert).mapLeft {
                val inputExplanation = getInputExplanation()

                val callEnv = getCallsBefore(
                    methodAContext.methodCallId,
                    maxOrd = null
                )
                EquivalenceChecker.SatInterpretation.RealCounterExample(
                    ruleCheckResult = ruleResult,
                    diffExplanation = it,
                    inputExplanation = inputExplanation,
                    priorEvents = callEnv
                )
            }.toValue({ it }, { EquivalenceChecker.SatInterpretation.GaveUp(it, ruleResult) })
        }

        fun fail(f: () -> String) : EquivalenceChecker.SatInterpretation {
            logger.info(f)
            return EquivalenceChecker.SatInterpretation.GaveUp(f(), ruleResult)
        }

        /**
         * Otherwise, find out which index in our trace has the mismatch.
         */
        val eventIdx = vcProgram.parallelLtacStream().mapNotNull {
            it.maybeAnnotation(EquivalenceChecker.IndexHolder.META_KEY)
        }.mapNotNull {
            theModel.valueAsBigInteger(it.indexSym).leftOrNull()
        }.collect(Collectors.toSet()).singleOrNull() ?: return fail {
            "Couldn't find single event id"
        }
        /**
         * Trace is already minimal, skip to [postMinimizationAnalysis]
         */
        if(eventIdx == BigInteger.ZERO) {
            return postMinimizationAnalysis(
                eventIdx
            )
        } else {
            /**
             * Otherwise, try to find an earlier trace, if we can't, keep going in [postMinimizationAnalysis]
             */
            return EquivalenceChecker.SatInterpretation.Refine(
                TraceMinimizer(
                    idx = eventIdx,
                    traceLevel = instLevels,
                    context
                ) {
                    postMinimizationAnalysis(
                        eventIdx
                    )
                }
            )
        }
    }

    private fun <T: EquivalenceChecker.METHOD_MARKER> tryExtractBufferModel(
        event: EquivalenceChecker.LTraceEventMarker<T>
    ) : Either<List<UByte>, String> {
        return theModel.valueAsBigInteger(event.marker.lengthVar).fmtError().bindLeft { len ->
            theModel.valueAsBigInteger(event.marker.bufferStart).fmtError().bindLeft { base ->
                PreciseBufferExtraction.extractBufferModel(
                    graph = vcProgram.analysisCache.graph,
                    model = theModel,
                    where = event.vcProgramSite,
                    len = len,
                    start = base,
                    buffer = event.marker.bufferBase
                ).toList(len)
            }
        }
    }

    /**
     * Kotlin doesn't have a Quarduple class, so I use this instead.
     * Used to indicate which method is [missing] the event [lt] that was found
     * in [found]. [explain] describes how to turn that event data into a [verifier.equivalence.EquivalenceChecker.MismatchExplanation].
     */
    private data class MissingPayload(
        val missing: TACMethod,
        val found: TACMethod,
        val lt: EquivalenceChecker.LTraceWithContext<*>,
        val explain: (EquivalenceChecker.EventWithData) -> EquivalenceChecker.MismatchExplanation,
    )

    /**
     * From the [BufferTraceInstrumentation.TraceIndexMarker],
     * extract the [verifier.equivalence.EquivalenceChecker.EventWithData] representation,
     * including sort information, parameter info, etc.
     */
    private fun traceMarkerToEvent(
        lTraceEventMarker: EquivalenceChecker.LTraceEventMarker<*>
    ) : Either<EquivalenceChecker.EventWithData, String> {
        val event = BufferTraceInstrumentation.extractEvent(
            theModel = theModel,
            vcProgram = vcProgram,
            where = lTraceEventMarker.vcProgramSite,
            marker = lTraceEventMarker.marker
        ).leftOr { return it }
        val sort = event.sort
        val params = when(event) {
            is BufferTraceInstrumentation.RawEventParams.CallParams -> {
                listOf(
                    EquivalenceChecker.ExternalEventParam(
                        label = EquivalenceChecker.ContextLabel.CALLEE,
                        value = event.callee.mapLeft {
                            "0x${it.toString(16)}"
                        }.leftOrNull()
                    ),
                    EquivalenceChecker.ExternalEventParam(
                        label = EquivalenceChecker.ContextLabel.CALL_VALUE,
                        value = event.value.mapLeft {
                            it.toString()
                        }.leftOrNull()
                    )
                )
            }
            is BufferTraceInstrumentation.RawEventParams.ExitParams -> listOf()
            is BufferTraceInstrumentation.RawEventParams.LogTopics -> {
                event.params.mapIndexed { ind, either ->
                    val t = when(ind) {
                        0 -> EquivalenceChecker.ContextLabel.LOG_TOPIC1
                        1 -> EquivalenceChecker.ContextLabel.LOG_TOPIC2
                        2 -> EquivalenceChecker.ContextLabel.LOG_TOPIC3
                        3 -> EquivalenceChecker.ContextLabel.LOG_TOPIC4
                        else -> error("implausible number of topics")
                    }
                    EquivalenceChecker.ExternalEventParam(
                        label = t,
                        value = either.mapLeft { "0x${it.toString(16)}" }.leftOrNull()
                    )
                }
            }
        }
        val buffer = tryExtractBufferModel(lTraceEventMarker).leftOrNull()
        return EquivalenceChecker.BasicEvent(
            params = params,
            sort = sort,
            bufferRepr = buffer
        ).toLeft()
    }

    /**
     * Before event at [reprMethod], find all prior calls/logs.
     */
    private fun getPriorTrace(
        reprMethod: EquivalenceChecker.LTraceWithContext<*>,
    ) : Either<List<EquivalenceChecker.IEvent>, String> {
        /**
         * The prior calls are just those with ordinal < this event index
         */
        if(this.instLevels.traceLevel == BufferTraceInstrumentation.TraceTargets.Calls) {
            return getCallsBefore(reprMethod.context.methodCallId, reprMethod.eventIndex.intValueExact()).toLeft()
        }
        /**
         * Get the number of calls recorded in this event marker, and get those.
         */
        val callOrd = theModel.valueAsBigInteger(reprMethod.trace.marker.numCalls).withFailureString(
            "Could not extract the number of prior calls before the event in question"
        ).leftOr { return it }.intValueExact()
        val priorCalls = getCallsBefore(reprMethod.context.methodCallId, callOrd)
        /**
         * We ignore logs when looking at results (maybe we shouldn't?)
         */
        if(this.instLevels.traceLevel == BufferTraceInstrumentation.TraceTargets.Results) {
            return priorCalls.toLeft()
        }
        check(this.instLevels.traceLevel == BufferTraceInstrumentation.TraceTargets.Log)
        /**
         * Find the interleaving of calls/logs.
         *
         * We actually allow this interleaving to be different between implementations, so showing this
         * as a unified trace is a little misleading.
         */
        val eventList = mutableListOf<EquivalenceChecker.IEvent>()
        var currentCallCount = 0
        var eventIt = BigInteger.ZERO
        while(eventIt < reprMethod.eventIndex) {
            val r = when(val repr = extractEventData(
                reprMethod.context,
                vcProgram, theModel, eventIt
            )) {
                is MatchingEventData.Missing -> {
                    return "Failed to find event information for the $eventIt event".toRight()
                }
                is MatchingEventData.Found -> repr.what
            }

            val numCallsAtEvent = theModel.valueAsBigInteger(r.marker.numCalls).withFailureString(
                "Failed to get number of calls at $eventIt event"
            ).leftOr {
                return it
            }.intValueExact()
            while(currentCallCount < numCallsAtEvent) {
                eventList.add(priorCalls[currentCallCount])
                currentCallCount++
            }
            val env = traceMarkerToEvent(r).leftOr {
                return "Failed to extract data for $eventIt: ${it.right()}".toRight()
            }
            eventList.add(env)
            eventIt++
        }
        while(currentCallCount < callOrd) {
            eventList.add(priorCalls[currentCallCount++])
        }
        return eventList.toLeft()
    }

    /**
     * Try to explain what's missing and from which function.
     */
    private fun tryMissingInterpretation(
        eventIndex: BigInteger,
        methodAEvent: MatchingEventData<EquivalenceChecker.LTraceEventMarker<EquivalenceChecker.METHODA>>,
        methodAContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODA>,
        methodBEvent: MatchingEventData<EquivalenceChecker.LTraceEventMarker<EquivalenceChecker.METHODB>>,
        methodBContext: EquivalenceChecker.InlinedInstrumentation<EquivalenceChecker.METHODB>
    ): EquivalenceChecker.SatInterpretation {
        val inputExplanation = getInputExplanation()
        val (_, foundMethod, event, mk) = when(methodAEvent) {
            is MatchingEventData.Found -> {
                MissingPayload(
                    missing = methodB,
                    found = methodA,
                    explain = EquivalenceChecker.MismatchExplanation::MissingInB,
                    lt = EquivalenceChecker.LTraceWithContext(eventIndex, methodAEvent.what, methodAContext)
                )
            }
            MatchingEventData.Missing -> {
                check(methodBEvent is MatchingEventData.Found)
                MissingPayload(
                    missing = methodA,
                    found = methodB,
                    explain = EquivalenceChecker.MismatchExplanation::MissingInA,
                    lt = EquivalenceChecker.LTraceWithContext(eventIndex, methodBEvent.what, methodBContext)
                )
            }
        }

        /**
         * The event we found in foundMethod that was missing
         */
        val basicEvent = traceMarkerToEvent(event.trace).leftOr {
            return EquivalenceChecker.SatInterpretation.GaveUp(
                "Couldn't extract event data from ${foundMethod.pp()}: ${it.right()}",
                ruleResult
            )
        }

        val priorEvents = getPriorTrace(event).leftOrNull()

        return EquivalenceChecker.SatInterpretation.RealCounterExample(
            ruleCheckResult = ruleResult,
            diffExplanation = mk(basicEvent),
            priorEvents = priorEvents,
            inputExplanation = inputExplanation
        )

    }
}
