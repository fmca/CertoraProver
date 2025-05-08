/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY, without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR a PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

 contract Summary {
    uint public foo = 2;

    struct Data{
        uint x;
    }

    function internalCall() internal returns (uint) {
        return 4;
    }

    function setFooConditionally(Summary.Data memory data) public {
        if(data.x > 1){
            foo = internalCall();
            return;
        }
        foo = 5;
    }

    function unresolvedCall(address token) external {
        (bool success, bytes memory result) = token.call(abi.encodeWithSignature("bar()"));
        require(success);
        foo = abi.decode(result, (uint256));
    }

    function setFoo() public {
        foo = 2;
    }
}