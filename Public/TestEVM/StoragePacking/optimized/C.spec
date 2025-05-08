using C as C;

methods {
	function a(uint) external returns (uint32) envfree;
	function len() external returns (uint256) envfree;
}


rule check1() {
	require len() == 2;
	require C.a[0] != C.a[1];
	assert a(0) != a(1);
}
