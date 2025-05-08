methods {
    function foo(uint) external envfree;
}

function sqrtCVLPostcondition(uint256 x) returns uint256 {
    uint256 z;
    require (z^2 <= x && (z+1)^2 > x, "Computation of square root via requiring, this is ok.");
    return z;
}

rule requireSomethingDirectlyWithReason {
    uint x;
    require(x < 100, "This is my very good reason for this assumption");
    require x > 20, "This is my other very good reason in other syntax";
    foo(x);
    assert true;
}

rule requireSomethingDirectlyWithoutReason {
    uint x;
    require(x < 10);
    foo(x);
    assert true;
}

rule requireWithinCalledCVLFunction {
    uint x;
    uint root = sqrtCVLPostcondition(x);
    foo(root);
    assert true;
}
