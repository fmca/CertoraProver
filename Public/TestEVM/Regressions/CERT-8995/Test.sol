
contract Test {
	uint256 constant my_selector = 0xdeadbeef;

	function getThing(address other, uint value) internal returns (uint toRet) {
		assembly {
			mstore(0x0, my_selector)
			mstore(0x20, value)
			if iszero(staticcall(gas(), other, 0x1c, 0x24, 0x00, 0x20)) {
				revert(0,0)
			}
            toRet := mload(0x0)
		}
	}

	function summarizeMe(address other, uint value) internal returns (uint) {
		return getThing(other, value);
	}

	function doOtherThing(uint a) internal returns (uint) {
		return a + 1;
	}

	modifier blowStack(uint a) {
		_;
		assembly {
			log1(a, 0,0)
		}
	}

	/**
	 * What is with this weird repetition? Well, it turns out you have to work pretty hard to get the
	 * auto generated indices and stack heights to hash in a way that makes the temp variable generated in
	 * getThing to be chosen as the return value alias. This is the configuration I found through kinda brute force.
	 */
	function useSummary(address other, uint value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value) blowStack(value)  external returns (uint) {
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);
		summarizeMe(other, value);

		return doOtherThing(summarizeMe(other, value));
	}
}
