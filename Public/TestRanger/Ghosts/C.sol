contract C {
    mapping (address => mapping ( address => uint256)) public m;

    function set_m(address a, address b, uint256 u) external { m[a][b] = u; }
}
