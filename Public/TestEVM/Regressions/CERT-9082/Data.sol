// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

import { Foo } from "./Foo.sol";

contract Data {
    struct Storage {
        Foo foo;
    }

    Storage private s;

    function getFoo() public view returns (Foo) {
        return s.foo;
    }
}
