# 747. Largest Number At Least Twice of Others
# in python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i in nums:
            if i != m and m < 2 * i:
                return -1
        return nums.index(m)

# in java
class Solution {
    public int dominantIndex(int[] nums) {
        int max1 = -1, max2 = -1;
        int idx = -1;

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (num > max1) {
                max2 = max1;
                max1 = num;
                idx = i;
            } else if (num > max2) {
                max2 = num;
            }
        }

        return (max1 >= 2 * max2) ? idx : -1;
    }
}
