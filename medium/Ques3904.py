# 3904. Smallest Stable Index II         (Explanation -> same as prob. 3903)
# in python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * n

        mn = float("inf")
        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            suffix[i] = mn

        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            score = mx - suffix[i]
            if score <= k:
                return i

        return -1

# in java
class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        int[] suffix = new int[n];

        int min = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            min = Math.min(min, nums[i]);
            suffix[i] = min;
        }

        int max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
            int score = max - suffix[i];
            if (score <= k)
                return i;
        }

        return -1;
    }
}
