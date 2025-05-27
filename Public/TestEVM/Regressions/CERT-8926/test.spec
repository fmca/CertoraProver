methods {
    function _.balance(bytes32) external => 3 expect uint;
}

rule test {
    env e;
    bytes arg;
    address a;
    assert entry(e, arg, a) == 3;
}