contract Test {
	function entryPoint(uint x) external returns (bytes32) {
		return keccak256(implicitLoop()[x]);
	}

	function implicitLoop() internal returns (bytes[16] memory ret) {
		ret[0] = abi.encodePacked(msg.sender);
	}
}
