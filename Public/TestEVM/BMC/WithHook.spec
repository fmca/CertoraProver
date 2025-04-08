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

using InvParams as c;

function isInRange(address someContract, uint y) returns bool {
    if (someContract != c) return true;

    return c.foo <= y;
}

invariant succeedingWithHook(env invParam, uint x) x >= 5 => isInRange(c, x) {
    preserved setFooConditionally(InvParams.Data data) with (env e) {
        require invParam.msg.sender != e.msg.sender;
        require data.x == 0;
    }
}

hook Sload uint value c.bar {
    require value != 8;
}