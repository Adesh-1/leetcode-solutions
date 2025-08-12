// 198. House Robber
// in java
class Solution {
    public int rob(int[] nums) {
        int rob = 0;
        int skip = 0;
        for (int num : nums) {
            int newRob = skip + num;
            skip = Math.max(skip, rob);
            rob = newRob;
        }
        return Math.max(skip, rob);
    }
}

// in python
class Solution:
    def rob(self, nums: List[int]) -> int:
        r = s = 0
        for i in nums: r, s = s + i, max(s, r)
        return max(r, s)
