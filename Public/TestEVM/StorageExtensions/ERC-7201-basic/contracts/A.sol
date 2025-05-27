import {TwoPair} from "../types/TwoPair.sol";

contract A {

   /** @custom:storage-location erc7201:a.data */
   struct AData {
     TwoPair tp;
     uint x;
   }

   //keccak256(abi.encode(uint256(keccak256("a.data")) - 1)) & ~bytes32(uint256(0xff));
   bytes32 private constant A_DATA_LOC = 0x9cf04d36fde00bc904be52881850b7532174cd0bf4e1b99dbcc18bb69cbdbd00;

   function getData() internal pure returns (AData storage $) {
     assembly {
       $.slot := A_DATA_LOC
     }
   }
}
