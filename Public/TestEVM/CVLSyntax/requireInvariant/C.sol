contract C {
    struct Foo{
        uint256 a;
        uint256 b;
    }
    uint256 public foo;
    uint256 public bar;
    address public addr;

    function get() public returns (Foo memory){
        return Foo(10,10);
    }

    function getAddress(address foo) public returns (address){
        return foo;
    }
}
