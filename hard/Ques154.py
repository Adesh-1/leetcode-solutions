# 154. Find Minimum in Rotated Sorted Array II
# in python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

  # in java
  class Solution {
    public int findMin(int[] nums) {
        int min = nums[0];
        for (int i : nums) {
            if (min > i) // for ex if '3 > 1' then
                min = i;
        }
        return min;
    }
}
