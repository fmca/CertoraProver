methods {
	function Test.summarizeMe(address,uint) internal returns (uint) => 44;
}

rule test(address a, uint value) {
	env e;
	assert useSummary(e, a, value) == 45;
}
