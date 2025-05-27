interface IERC20 {
    function transferFrom(address, address, uint256) external;
}

contract Orig {
    // taken from solady
    function safeTransferFrom(
        address token,
        address from,
        address to,
        uint256 amount
    ) internal {
        /// @solidity memory-safe-assembly
        assembly {
            let m := mload(0x40) // Cache the free memory pointer.
            mstore(0x60, amount) // Store the `amount` argument.
            mstore(0x40, to) // Store the `to` argument.
            mstore(0x2c, shl(96, from)) // Store the `from` argument.
            mstore(0x0c, 0x23b872dd000000000000000000000000) // `transferFrom(address,address,uint256)`.
            let success := call(gas(), token, 0, 0x1c, 0x64, 0x00, 0x20)
            if iszero(and(eq(mload(0x00), 1), success)) {
                if iszero(
                    lt(
                        or(iszero(extcodesize(token)), returndatasize()),
                        success
                    )
                ) {
                    mstore(0x00, 0x7939f424) // `TransferFromFailed()`.
                    revert(0x1c, 0x04)
                }
            }
            mstore(0x60, 0) // Restore the zero slot to zero.
            mstore(0x40, m) // Restore the free memory pointer.
        }
    }

    function entry(
        address token,
        address from,
        address to,
        uint256 amount
    ) external {
        safeTransferFrom(token, from, to, amount);
    }
}

contract Simple {
    function safeTransferFrom(
        address token,
        address from,
        address to,
        uint256 amount
    ) internal {
        bool success;
        bytes memory returnData;

        (success, returnData) = token.call(
            abi.encodeWithSelector(
                IERC20.transferFrom.selector,
                from,
                to,
                amount
            )
        );

        // The original logic uses this exact check
        assembly {
            // Check if call succeeded AND returned 1
            let validCall := and(eq(mload(add(returnData, 32)), 1), success)

            if iszero(validCall) {
                // Logic for determining whether to revert
                let hasNoCode := iszero(extcodesize(token))
                let returnSize := mload(returnData) // First 32 bytes of returnData is length

                // Original: if iszero(lt(or(iszero(extcodesize(token)), returndatasize()), success))
                let skipRevert := lt(or(hasNoCode, returnSize), success)

                if iszero(skipRevert) {
                    // Revert with TransferFromFailed()
                    mstore(0x00, 0x7939f424)
                    revert(0x1c, 0x04)
                }
            }
        }
    }
    function entry(
        address token,
        address from,
        address to,
        uint256 amount
    ) external {
        safeTransferFrom(token, from, to, amount);
    }
}
