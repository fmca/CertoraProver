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

struct Foo {
    uint128 bar;
}
using FooLib for Foo global;

library FooLib {
    function getAndAdd(
        Foo storage $,
        uint40 param
    ) internal returns (uint128, uint40) {
        uint40 res;
        if(param == type(uint40).max){
            res = param;
        } else{
            res = param + 1;
        }
        return ($.bar + param, res);
    }
}

contract C {
    Foo internal foo;
    uint bar = 10;

    function getAndAdd(uint40 param) external returns (uint40)  {
        (uint128 a, uint40 b) = foo.getAndAdd(param);
        bar = a;
        return (b);
    }

    function setBar() external {
        bar = 2;
    }
}