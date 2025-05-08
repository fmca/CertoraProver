methods {
    function assertEq(uint a, uint b) internal => assertEqSummary(a, b);
}

function assertEqSummary(uint a, uint b) {
    assert a == b;
}

rule r {
    env e;
    uint n = testRoll(e, false, 0);
    testRoll(e, true, n);
    assert true;
}
