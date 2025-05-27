interface Intf {
    function balance(bytes32) external returns (uint);
}

contract Test {
    function entry(bytes memory mem, address a) external returns (uint) {
        require(mem.length == 32);
        uint prefix = 0;
        for(uint i = 0; i < mem.length; i++) {
            if(mem[0] == 0) {
                break;
            }
            prefix++;
        }
        require(prefix != 0);
        bytes memory toRet = new bytes(prefix);
        for(uint i = 0; i < prefix; i++) {
            toRet[i] = mem[i];
        }
        string memory cast = string(toRet);
        bytes32 arg = keccak256(bytes(cast));
        return Intf(a).balance(arg);
    }
}