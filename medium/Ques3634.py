# 3634. Minimum Removals to Balance Array
# in python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        l = 0
        max_len = 1
        
        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return n - max_len

# in java
class Solution {
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int l = 0;
        int ml = 1;
        for (int i = 0; i < n; i++) {
            while (nums[i] > (long) nums[l] * k)
                l++;
            ml = Math.max(ml, i - l + 1);
        }
        return n - ml;
    }
}
