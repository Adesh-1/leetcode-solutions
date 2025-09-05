# 162. Find Peak Element
# in pyhton
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))

  # in java
  class Solution {
    public int findPeakElement(int[] nums) {
        int maxVal = nums[0], ind = 0; # //initialize first value and index
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > maxVal){
                maxVal = nums[i];
                ind = i;
            }        
        }
        return ind;
    }
}
