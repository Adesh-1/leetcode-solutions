# 2770. Maximum Number of Jumps to Reach the Last Index
# in python
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp[i] = maximum jumps needed to reach i
        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            # if current index is unreachable
            if dp[i] == -1:
                continue

            for j in range(i + 1, n):

                # valid jump condition
                if abs(nums[j] - nums[i]) <= target:

                    # update maximum jumps
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1]


# in java
class Solution {
    public int maximumJumps(int[] nums, int target) {
        int n = nums.length;

        int[] dp = new int[n];
        
        # // initialize with -1 (unreachable)
        Arrays.fill(dp, -1);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {

            # // skip unreachable index
            if (dp[i] == -1) continue;

            for (int j = i + 1; j < n; j++) {

                if (Math.abs(nums[j] - nums[i]) <= target) {
                    dp[j] = Math.max(dp[j], dp[i] + 1);
                }
            }
        }

        return dp[n - 1];
    }
}
