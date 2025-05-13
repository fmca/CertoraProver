ghost mapping(address => mapping(address => uint256)) g_m_mirror {
    init_state axiom forall address a. forall address b. g_m_mirror[a][b] == 0;
}
ghost mapping(address => mathint) g_m_sum {
    init_state axiom forall address a. g_m_sum[a] == 0;
    init_state axiom forall address a. (usum address b. g_m_mirror[a][b]) == 0;
}

hook Sstore currentContract.m[KEY address a][KEY address b] uint256 u {
    g_m_mirror[a][b] = u;
    g_m_sum[a] = g_m_sum[a] + u;
}

invariant checkSum(address a) (usum address b. g_m_mirror[a][b]) == g_m_sum[a];
