# 2897. Apply Operations on Array to Maximize Sum of Squares
# in python
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 31

        # Count how many numbers have each bit set
        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    bits[i] += 1

        ans = 0

        # Construct k numbers with the maximum possible set bits
        for _ in range(k):
            num = 0

            for i in range(31):
                # Use this bit if at least one copy is available
                if bits[i] > 0:
                    num |= 1 << i  # Turn on the ith bit
                    bits[i] -= 1  # Use one available copy of this bit

            # Add the square of the constructed number
            ans = (ans + num * num) % MOD

        return ans

# in java
class Solution {
    public int maxSum(List<Integer> nums, int k) {
        final int MOD = 1_000_000_007;
        int[] bits = new int[31];

        for (Integer num : nums) {
            for (int i = 0; i < 31; i++) {
                if ((num & (1 << i)) != 0)
                    bits[i] += 1;
            }
        }

        long ans = 0;

        for (int c = 0; c < k; c++) {
            int num = 0;

            for (int i = 0; i < 31; i++) {
                if (bits[i] > 0) {
                    num |= (1 << i);
                    bits[i] -= 1;
                }
            }

            ans = (ans + (long) num * num) % MOD;
        }
        return (int) ans;
    }
}
