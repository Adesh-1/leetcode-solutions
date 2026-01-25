// 1984. Minimum Difference Between Highest and Lowest of K Scores
// in java
class Solution {
    public int minimumDifference(int[] nums, int k) {
        if (k == 1)
            return 0;
        Arrays.sort(nums);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i + k - 1 < nums.length; i++) {
            int diff = nums[i + k - 1] - nums[i];
            minDiff = Math.min(minDiff, diff);
        }
        return minDiff;
    }
}

// in python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff = float("inf")
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)
        return min_diff
