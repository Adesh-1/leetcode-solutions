// 3524. Find X Value of Array I
// in java
class Solution {
    public long[] resultArray(int[] nums, int k) {
        long[] ans = new long[k];
        long[] dp = new long[k];

        for (int num : nums) {

            long[] newDp = new long[k];

            // Extend previous subarrays
            for (int r = 0; r < k; r++) {
                int newRemainder = (r * (num % k)) % k;
                newDp[newRemainder] += dp[r];
            }

            // Start a new subarray with only num
            newDp[num % k]++;

            // Move to the next position
            dp = newDp;

            // Add current subarrays to the answer
            for (int r = 0; r < k; r++) {
                ans[r] += dp[r];
            }
        }

        return ans;
    }
}

// in python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            newdp = [0] * k

            for i in range(k):
                n_r = (i * (num % k)) % k
                newdp[n_r] += dp[i]

            newdp[num % k] += 1
            dp = newdp

            for i in range(k):
                ans[i] += dp[i]

        return ans
