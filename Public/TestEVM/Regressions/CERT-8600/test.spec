rule should_fail {
	env e;
	uint x;
	entryPoint(e, x);
	assert false;
}
