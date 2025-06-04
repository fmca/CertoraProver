contract A {
	function different() external {
		revert("OH NO BIG ERROR THIS STRING SHOULD BE PRETTY LONG TO PUT IT IN CODEDATA");
	}

	function same() external {
		revert("OH NO AN EVEN BIGGER ERROR MESSAGE STRING THAT NEEDS TO BE > 32 BYTES");
	}
}

contract B {
	function same() external {
		revert("OH NO AN EVEN BIGGER ERROR MESSAGE STRING THAT NEEDS TO BE > 32 BYTES");
	}

	function different() external {
		revert("OH NO BIG ERROR THIS STRING SHOULD BE PRETTY LONG TO PUT IT IN CODED4TA");
	}
}
