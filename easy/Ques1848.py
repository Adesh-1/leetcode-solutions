# 1848. Minimum Distance to the Target Element
# in python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, x in enumerate(nums) if x == target)

# in java
class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target)
                ans = Math.min(ans, Math.abs(i - start));
        }
        return ans;
    }
}
