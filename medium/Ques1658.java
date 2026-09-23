// 1658. Minimum Operations to Reduce X to Zero
// in python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target == 0:
            return n

        left = total = max_len = 0

        for right, num in enumerate(nums):
            total += num

            while left <= right and total > target:
                total -= nums[left]
                left += 1

            if total == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == 0 else n - max_len

// in java
class Solution {
    public int minOperations(int[] nums, int x) {
        int n = nums.length;

        // Find total sum
        int total = 0;
        for (int num : nums) {
            total += num;
        }

        // Sum that we want to keep
        int target = total - x;

        // If target is 0, we need to remove everything
        if (target == 0) {
            return n;
        }

        int left = 0;
        int sum = 0;
        int maxLen = -1;

        // Sliding window
        for (int right = 0; right < n; right++) {
            sum += nums[right];

            // Reduce window if sum becomes too large
            while (left <= right && sum > target) {
                sum -= nums[left];
                left++;
            }

            // Found a subarray with required sum
            if (sum == target) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }

        // No valid subarray found
        if (maxLen == -1) {
            return -1;
        }

        // Remove everything outside the longest valid subarray
        return n - maxLen;
    }
}
