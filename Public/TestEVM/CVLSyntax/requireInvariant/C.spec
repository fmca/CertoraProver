invariant invariantFooWithParam(uint val) currentContract.foo >= val;
invariant invariantFoo() currentContract.foo >= 10;
invariant invariantBar() currentContract.bar >= 5;
invariant invariantWithStruct(C.Foo val) currentContract.foo >= val.a;
invariant invariantWithAddr(address val) currentContract.addr == val;

function safeAssumptions() {
	requireInvariant invariantFoo();
}

rule shouldFail_requireInvariantWithAddr_after_assert2() {
    address baz;
	env e;
	assert currentContract.addr == baz;
	requireInvariant invariantWithAddr(getAddress(e, baz));
	assert true;
}

rule shouldSucceed_requireInvariantInCVLFunction() {
	safeAssumptions();
	assert currentContract.foo >= 5;
	assert true;
}

rule shouldFail_requireInvariantWithAddr_after_assert0() {
    address baz;
	assert currentContract.addr == baz;
	requireInvariant invariantWithAddr(baz);
	assert true;
}

rule shouldFail_requireInvariantWithStruct_after_assert0() {
    env e;
    C.Foo foo = get(e);
	assert currentContract.foo >= 5;
	requireInvariant invariantWithStruct(foo);
	assert true;
}

rule shouldFail_requireInvariantWithStruct_after_assert10() {
    env e;
    C.Foo foo = get(e);
	assert currentContract.foo >= 5;
	requireInvariant invariantFooWithParam(foo.a);
	assert true;
}

rule shouldFail_requireInvariantWithParam_after_assert0() {
	assert currentContract.foo >= 5;
	requireInvariant invariantFooWithParam(10);
	assert true;
}

rule shouldFail_requireInvariantWithParam_after_assert1() {
    uint x;
    require(x >= 10);
	assert currentContract.foo >= 5;
	requireInvariant invariantFooWithParam(x);
	assert true;
}

rule shouldFail_requireInvariantWithParam_after_assert2(uint x) {
    require(x >= 10);
	assert currentContract.foo >= 5;
	requireInvariant invariantFooWithParam(x);
	assert true;
}

rule shouldSucceed_requireInvariantWithParam_before_assert() {
	requireInvariant invariantFooWithParam(10);
	assert currentContract.foo >= 5;
}

rule shouldSucceed_requireInvariant_after_assert() {
	assert currentContract.foo >= 5;
	requireInvariant invariantFoo();
	assert true;
}

rule shouldSucceed_requireInvariant_before_assert() {
	requireInvariant invariantFoo();
	assert currentContract.foo >= 5;
}

rule shouldSucceed_twoRequireInvariantCommands() {
	assert currentContract.foo >= 5 && currentContract.bar >= 3;
	requireInvariant invariantFoo();
	requireInvariant invariantBar();
	assert true;
}

rule shouldFail_twoRequireInvariantCommands() {
	assert currentContract.foo >= 5 && currentContract.bar >= 6;
	requireInvariant invariantFoo();
	requireInvariant invariantBar();
	assert true;
}