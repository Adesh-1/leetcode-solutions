# 3653. XOR After Range Multiplication Queries I
# in python
class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7

        # Process each query
        for li, ri, ki, vi in queries:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki

        # Compute XOR of final array
        result = 0
        for num in nums:
            result ^= num

        return result

# in java
class Solution {
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int MOD = 1000000007;

        # // Process each query
        for (int[] q : queries) {
            int li = q[0];
            int ri = q[1];
            int ki = q[2];
            int vi = q[3];

            int idx = li;
            while (idx <= ri) {
                nums[idx] = (int)((1L * nums[idx] * vi) % MOD);
                idx += ki;
            }
        }

        # // Compute XOR
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }

        return result;
    }
}
