# 724. Find Pivot Index
# in python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i, num in enumerate(nums):
            if left == total - left - num:   # or 'left * 2 + num == total'
                return i
            left += num

        return -1

# in java
class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        for (int num : nums)
            total += num;

        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            int rightSum = total - nums[i] - leftSum;
            if (rightSum == leftSum)
                return i;
            leftSum+=nums[i];
        }

        return -1;
    }
}
