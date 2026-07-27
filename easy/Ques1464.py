# 1464. Maximum Product of Two Elements in an Array
# in python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)

# in java
class Solution {
    public int maxProduct(int[] nums) {
        int f = 0, s = 0;
        for (int i : nums) {
            if (i > f) {
                s = f;
                f = i;
            } else if (i > s)
                s = i;
        }
        return (f - 1) * (s - 1);
    }
}
