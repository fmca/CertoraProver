library Library1 {
	function toSummarize() external returns (uint) {
		return 1;
	}
}

library Library2 {
	function toSummarize() external returns (uint) {
		return 2;
	}
}


library Library3 {
	function toSummarize() external returns (uint) {
		return 3;
	}
}


library Library4 {
	function toSummarize() external returns (uint) {
		return 4;
	}
}

library Library5 {
	function toSummarize() external returns (uint) {
		return 5;
	}
}

contract Test {

    function nondetSummary() external returns (uint) {
        return Library1.toSummarize();
    }

    function havocAllSummary() external returns (uint) {
        return Library2.toSummarize();
    }

    function havocECFSummary() external returns (uint) {
        return Library3.toSummarize();
    }

    function autoSummary() external returns (uint) {
        return Library4.toSummarize();
    }

	function unresolvedExternalSummary(address target, bytes memory data) external returns (uint256) {
        (bool success, bytes memory x) = address(target).call(data);
        if(success){
            return bytesToUint(x);
        } else {
            return 0;
        }
    }

    function unresolvedExternalSummaryDefault(address target, bytes memory data) external returns (uint256) {
        (bool success, bytes memory x) = address(target).call(data);
        if(success){
            return bytesToUint(x);
        } else {
            return 0;
        }
    }

    function toSummarize() external returns (uint256) {
        return 5;
    }

    function getToSummarizeFunctionSelector() external returns (bytes memory) {
        return abi.encodeWithSignature("toSummarize()");
    }

    function bytesToUint(bytes memory b) public pure returns (uint) {
        require(b.length == 32);

        uint res;
        assembly {
            res := mload(add(b, 0x20))
        }
        return res;
    }
}
