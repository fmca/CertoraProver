methods {
    function Test.externalTwo(Test.LocalVars) external returns (bytes32) => to_bytes32(0);
}

rule call_resolution_works {
    env e;
    bytes[] init;
    bool someBool;
    assert doThings(e, init, someBool) == to_bytes32(0);
}