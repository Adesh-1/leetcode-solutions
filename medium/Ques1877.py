# 1877. Minimize Maximum Pair Sum in Array
# in python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) // 2):
            ans = max(ans, (nums[i] + nums[-i - 1]))
        return ans

# in java
class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n / 2; i++)
            ans = Math.max(ans, (nums[i] + nums[n - 1 - i]));
        return ans;
    }
}
