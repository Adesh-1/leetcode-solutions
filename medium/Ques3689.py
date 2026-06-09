# 3689. Maximum Total Subarray Value I
# in python
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))

# in java
class Solution {
    public long maxTotalValue(int[] nums, int k) {
        int mx = Integer.MIN_VALUE;
        int mn = Integer.MAX_VALUE;
        for (int i : nums) {
            mx = Math.max(mx, i);
            mn = Math.min(mn, i);
        }
        return 1L * k * (mx - mn);
    }
}
