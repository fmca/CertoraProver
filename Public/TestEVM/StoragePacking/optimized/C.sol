contract C {
    uint32[] public a;

    function len() public view returns (uint256) {
        return a.length;
    }

    function ff() public view returns (uint256) {
        uint256 sum;
        for (uint256 i = 0; i < a.length; i++) {
            sum = sum + a[i];
        }
        return sum;
    }

    function pp(uint32 value) public {
        a.push(value);
    }
}
