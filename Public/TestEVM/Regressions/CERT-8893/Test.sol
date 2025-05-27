contract Test {
	function doMcopy(uint sz, uint[] memory offsets, bytes[] memory sources) external returns (bytes memory) {
		bytes memory output = new bytes(sz);
		require(offsets.length == sources.length);
		for(uint i = 0; i < offsets.length; i++) {
			uint offsetO = offsets[i];
			uint offset = offsetO + 32;
			bytes memory source = sources[i];
			uint len = sources[i].length;
			require(offsetO + len <= output.length);
			assembly {
				mcopy(add(output, offset), add(source, 32), len)
			}
		}
		return output;
	}
}
