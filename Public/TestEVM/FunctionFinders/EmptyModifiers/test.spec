methods {
	function Test.int_f(string memory) internal returns (uint) => 4;
}

rule summary_works() {
	env e;
	string x;
	assert entry(e, x) == 4;
}
