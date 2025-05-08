/*
 *     The Certora Prover
 *     Copyright (C) 2025  Certora Ltd.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, version 3 of the License.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

package cvl

import org.junit.jupiter.api.Test

class TypeRuleTsets: CVLTestHarness() {
    @Test
    fun testCondExpError() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    bytes32 x;
                    bytes32 y = b ? x : 0;
                    assert true;
                """.trimIndent()
            ),
            "One branch of conditional must be a subtype of the other, but got incompatible types bytes32 and 0"
        )
    }
    @Test
    fun testCondExpError2() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    bytes32 x;
                    address a;
                    bytes32 y = b ? x : a;
                    assert true;
                """.trimIndent()
            ),
            "One branch of conditional must be a subtype of the other, but got incompatible types bytes32 and address"
        )
    }
    @Test
    fun testCondExpError3() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    bytes32 y = b ? x : -1;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : -1` has type `int16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp3() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    int16 y = b ? x : -1;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError4() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    bytes32 y = b ? x : 1;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : 1` has type `int8`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp4() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    int8 y = b ? x : 1;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError5() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    uint8 w;
                    bytes32 y = b ? x : w;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : w` has type `int16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp5() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    uint8 w;
                    int16 y = b ? x : w;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError6() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int16 x;
                    uint8 w;
                    bytes32 y = b ? x : w;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : w` has type `int16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp6() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int16 x;
                    uint8 w;
                    int16 y = b ? x : w;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError7() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int16 x;
                    uint256 w;
                    bytes32 y = b ? x : w;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : w` has type `mathint`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp7() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int16 x;
                    uint256 w;
                    mathint y = b ? x : w;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError8() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    address x;
                    bytes32 y = b ? x : 0;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : 0` has type `address`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp8() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    address x;
                    address y = b ? x : 0;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError9() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    bytes32 y = b ? -1 : 1;
                    assert true;
                """.trimIndent()
            ),
            "`b ? -1 : 1` has type `int8`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp9() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 y = b ? -1 : 1;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError10() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint16 x;
                    int8 w;
                    bytes32 y = b ? x : w;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : w` has type `int24`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp10() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint16 x;
                    int8 w;
                    int24 y = b ? x : w;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError11() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    bytes32 y = b ? x : 1000;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : 1000` has type `uint16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp11() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    uint16 y = b ? x : 1000;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError12() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    bytes32 y = b ? x : 1000;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : 1000` has type `int16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp12() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    int16 y = b ? x : 1000;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError13() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    bytes32 y = b ? x : -1000;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : -1000` has type `int16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp13() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    int16 y = b ? x : -1000;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExpError14() {
        assertNotTypeChecksWithError(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    bytes32 y = b ? x : -1000;
                    assert true;
                """.trimIndent()
            ),
            "`b ? x : -1000` has type `int16`, which cannot be converted to the expected type `bytes32`."
        )
    }
    @Test
    fun testCondExp14() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    int16 y = b ? x : -1000;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExp15() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    int8 x;
                    int8 y = b ? x : -1;
                    assert true;
                """.trimIndent()
            )
        )
    }
    @Test
    fun testCondExp16() {
        assertTypeChecks(
            generateSingleParameterlessRule(
                """
                    bool b;
                    uint8 x;
                    uint8 y = b ? x : 1;
                    assert true;
                """.trimIndent()
            )
        )
    }
}
