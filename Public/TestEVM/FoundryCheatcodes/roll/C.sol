interface I {
    function roll(uint256 newBlockNumber) external;
}

contract C {
    I i;
    uint bn;
    function assertEq(uint a, uint b) internal pure {}

    function testRoll(bool secondCall, uint n) external returns (uint) {
        if (secondCall) {
            assertEq(bn + n, block.number);
        } else {
            bn = block.number;
        }

        // Simple roll usage
        i.roll(block.number + 1);
        assertEq(bn + n + 1, block.number);

        // block.number here should be the "new" value
        i.roll(block.number + 1);
        assertEq(bn + n + 2, block.number);

        // test consistency across function calls
        i.roll(block.number + 1);
        assertEq(bn + this.testRollCalled(n + 3), block.number);
        return n + 4;
    }

    function testRollCalled(uint n) external returns (uint) {
        assertEq(bn + n, block.number);
        i.roll(block.number + 1);
        assertEq(bn + n + 1, block.number);
        return n + 1;

    }
}
