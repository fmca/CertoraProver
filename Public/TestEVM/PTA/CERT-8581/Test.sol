contract Test {
    function test(uint[] memory a) external {
        uint[16] memory accum;
        uint idx = 0;
        for(uint i = 0; i < a.length; i++) {
            accum[idx] = a[i];
            idx++;
        }
    }
}