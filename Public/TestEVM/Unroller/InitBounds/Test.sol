contract Test {

	function test(bytes[5] memory input) public returns (bytes[5] memory) {
		input[0] = bytes("");
		return input;
	}
}
