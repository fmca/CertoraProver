methods {
    function accessInvariant(address) external returns (bool) envfree;
    function increase(address, int256) external envfree;
}

function safeAssumptions(address user){
    requireInvariant alwaysPositive(user);
}

ghost mapping(address => int256) ghostBalance{
    init_state axiom forall address a. ghostBalance[a] == 0;
}

hook Sstore currentContract.balance[KEY address a] int256 new_value (int256 old_value) {
    ghostBalance[a] = new_value;
}

hook Sload int256 value currentContract.balance[KEY address a] {
    require(ghostBalance[a] == value);
}

invariant alwaysPositive(address a)
    ghostBalance[a] >= 0;

hook Sload bool b currentContract.accessInvariant[KEY address user] {

    safeAssumptions(user);
}


rule shouldFail(address a) {
    bool assertVal = (ghostBalance[a] >= 0);
    assert assertVal;
    bool b = accessInvariant(a);
    assert true;
}

rule shouldSucceed(address a) {
    bool assertVal = (ghostBalance[a] >= 0);
    bool b = currentContract.accessInvariant(a);
    assert assertVal;
}

rule shouldSucceed2(address a) {
    int256 value;
    bool assertVal = (ghostBalance[a] >= 0);
    increase(a, value);
    bool b = currentContract.accessInvariant(a);
    assert assertVal;
}