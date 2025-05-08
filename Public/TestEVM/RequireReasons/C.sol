contract C {
    uint n;
    A a;
    function foo(uint x) external returns (bool) {
        n = x;
        return true;
    }
    function callBar(uint x) external returns (bool) {
        return a.bar(x) > 0;
    }
    function callBaz(uint x) external returns (bool) {
        return a.baz(x) > 0;
    }
}

contract A {
    function bar(uint256 a) public returns (uint256) {
        return 2 * a;
    }

    function baz(uint256 a) external returns (uint256) {
        return 2 * a;
    }
}
