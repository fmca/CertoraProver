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

using Summary as c;

methods {
    function _.bar() external => DISPATCHER(true);
}

persistent ghost mathint invocationCount{
    init_state axiom invocationCount == 0;
}

function cvlFunc() returns uint {
    invocationCount = invocationCount + 1;
    if(invocationCount > 2){
        return 10;
    } else{
        return 5;
    }
}

invariant violatedLessThanFive(env e) c.foo <= 5;