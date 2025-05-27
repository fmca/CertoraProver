import {A} from "./A.sol";
import {TwoPair} from "../types/TwoPair.sol";

contract B is A {
   function getX() public returns (uint) {
     return getData().x;
   }
}
