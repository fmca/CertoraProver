methods {
    function getCount() external returns (uint256) envfree;
    function increment() external;
    function decrement() external;
}

rule incrementIncreasesCountByOne() {
    env e;
    uint256 countBefore = getCount();
    increment(e);
    uint256 countAfter = getCount();
    assert countAfter == countBefore + 1, "increment should increase count by 1";
}

rule decrementDecreasesCountByOne() {
    env e;
    uint256 countBefore = getCount();
    decrement(e);
    uint256 countAfter = getCount();
    if (countBefore > 0) {
        assert countAfter == countBefore - 1, "decrement should decrease count by 1 when count > 0";
    } else {
        assert countAfter == countBefore, "decrement should not change count when count is 0";
    }
}
