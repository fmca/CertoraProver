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

invariant succeedingLessThanFive(env invParam) c.foo <= 5 {
    preserved setFooConditionally(InvParams.Data data) with (env e) {
        require invParam.msg.sender != e.msg.sender;
        require data.x == 0;
        require c.bar != 8;
    }
}

invariant violatedLessThanFive(env invParam) c.foo <= 5 {
    preserved setFooConditionally(InvParams.Data data) with (env e) {
        require invParam.msg.sender != e.msg.sender;
        require c.bar != 8;
    }
}

invariant succeedingLessThanFiveParamConditional(env invParam, uint x) x >= 5 => c.foo <= x {
    preserved setFooConditionally(InvParams.Data data) with (env e) {
        require invParam.msg.sender != e.msg.sender;
        require data.x == 0;
        require c.bar != 8;
    }
}

invariant violatedLessThanFiveParamConditionalWithRequire(env invParam, uint x) x >= 5 => c.foo <= x {
    preserved setFooConditionally(InvParams.Data data) with (env e) {
        require invParam.msg.sender != e.msg.sender;
        require data.x == 0;
        requireInvariant barAlwaysEight(invParam);
    }
}

invariant barAlwaysEight(env invParam) invParam.msg.sender == c && c.bar == 8;