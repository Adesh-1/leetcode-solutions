# 3010. Divide an Array Into Subarrays With Minimum Cost I
# in python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        rl = sorted(nums[1:])
        return nums[0] + rl[0] + rl[1]
      # in this nums is not modify rl (remaining list) makes a new list of nums[1:] then sort rl
        # then rl will be sorted not nums

# in java
class Solution {
    public int minimumCost(int[] nums) {
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < min1) {
                min2 = min1;
                min1 = nums[i];
            } else if (nums[i] < min2) {
                min2 = nums[i];
            }
        }
        return nums[0] + min1 + min2;
    }
}
