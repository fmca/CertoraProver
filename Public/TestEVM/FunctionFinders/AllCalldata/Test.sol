contract Test {
	function doKeccak(bytes calldata m) internal returns (bytes32) {
		return keccak256(m);
	}

	function doIt() external returns (bytes32) {
		return doKeccak(msg.data);
	}
}
