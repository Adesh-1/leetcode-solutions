# 2778. Sum of Squares of Special Elements
# in python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)

        for i, num in enumerate(nums, start=1):
            if not n % i:
                ans += num**2

        return ans

# in java
class Solution {
    public int sumOfSquares(int[] nums) {
        int ans = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++)
            if (n % (i + 1) == 0)
                ans += nums[i] * nums[i];

        return ans;
    }
}
