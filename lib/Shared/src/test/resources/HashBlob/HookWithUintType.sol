contract HookWithUintType {
   mapping (uint256 => uint256) blerp;
   uint256[] arr;
   function bloop(uint256 x) external returns (uint256) {
     return blerp[x];
  }
}
