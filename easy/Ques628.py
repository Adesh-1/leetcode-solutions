# 628. Maximum Product of Three Numbers
# in python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pro1 = nums[-1] * nums[-2] * nums[-3]
        pro2 = nums[0] * nums[1] * nums[-1]
        return max(pro1, pro2)

# in java
class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int pro1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
        int pro2 = nums[0] * nums[1] * nums[n - 1];
        return Math.max(pro1, pro2);
    }
}
