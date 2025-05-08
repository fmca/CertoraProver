methods {
    function foo(uint) external returns bool envfree;
    function callBar(uint) external returns bool envfree;
    function callBaz(uint) external returns bool envfree;
    function A.bar(uint256 a) internal returns (uint256) => barSummary(a);
    function A.baz(uint256 a) external returns (uint256) => bazSummary(a);
}

rule directRequire(uint256 a) {
	require a != 0; // this is a function-input require since a is passed to foo
	assert foo(a); //foo is a solidity function
}

rule transitiveRequire(uint256 a) {
	require a != 0; // function-input require since a affects b which is passed to foo
	uint256 b = require_uint256(2 * a);
	assert foo(b); //foo is a solidity function
}

function factor(uint256 a, uint256 b) returns uint256 {
	require a != 0; //is function-input for helperFunctionRequire, but non-function-input for helperStorageRequire.
	return require_uint256(a * b);
}

rule helperStorageRequire(uint256 a, uint256 b) {
	require currentContract.n == factor(a, a); // non-function-input require
	assert foo(b);
}

rule helperFunctionRequire(uint256 a) {
	uint256 b = factor(a, a);
	assert foo(b);
}

function barSummary(uint256 a) returns uint256 {
	require a != 0; // non-function-input require, even though barSummary may affect the result of callBar().
	return require_uint256(2*a);
}

rule callWithSummaryIn(uint256 a) {
	assert callBar(a); // calls A.bar internally
}

function bazSummary(uint256 a) returns uint256 {
	require a != 0; // non-function-input require, even though bazSummary may affect the result of callBaz().
	return require_uint256(2*a);
}

rule callWithExternalSummaryIn(uint256 a) {
	assert callBaz(a); // calls A.baz internally
}
