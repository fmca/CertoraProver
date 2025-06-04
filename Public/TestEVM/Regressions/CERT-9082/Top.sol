// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

import { Data } from "./Data.sol";

contract Top {
    Data public immutable dataProvider;

    constructor(address _dataProvider) payable {
        dataProvider = Data(_dataProvider);
    }

    function testFoo() external view returns(uint256) {
        return dataProvider.getFoo().foo();
    }
}
