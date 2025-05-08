contract Test {
	uint64[] someArray;
	string someString;

	function doSomething() external returns (bytes32) {
		string memory someStringInMemory = someString;
		uint64[] memory someArrayInMemory = someArray;
		return keccak256(abi.encodePacked(someStringInMemory, someArrayInMemory));
	}
}
