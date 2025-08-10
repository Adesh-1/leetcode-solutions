// 1929. Concatenation of Array
// in python 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       nums.extend(nums)
       return nums

  // in java
  class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] n = new int[nums.length*2];
        for(int i = 0; i < nums.length; i++){
            n[i] = nums[i];
            n[nums.length+i] = nums[i];
        }
        return n;
    }
}
