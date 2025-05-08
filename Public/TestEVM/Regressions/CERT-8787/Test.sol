contract Test {
	struct LocalVars {
		bytes[3] scratchBuffers;
		uint a;
		bool keepGoing;
	}

	function doThings(bytes[] memory init, bool iterInit) external returns (bytes32) {
		LocalVars memory v;
		for(uint i = 0; i < init.length; i++) {
			v.scratchBuffers[i] = init[i];
		}
		v.keepGoing = iterInit;
		if(v.keepGoing) {
			v.scratchBuffers = this.externalOne(v);
			v.a++;
		}
		return this.externalTwo(v);
	}

	function externalTwo(LocalVars memory x) external returns (bytes32) {
		return keccak256(abi.encode(x));
	}

	function externalOne(LocalVars memory m) external returns (bytes[3] memory) {
		m.scratchBuffers[m.a] = bytes("");
		return m.scratchBuffers;
	}
}
