# 2567. Minimum Score by Changing Two Elements
# in python
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Case 1: Change two largest
        m1 = nums[n - 3] - nums[0]

        # Case 2: Change smallest and largest
        m2 = nums[n - 2] - nums[1]

        # Case 3: Change two smallest
        m3 = nums[n - 1] - nums[2]

        return min(m1, m2, m3)

# in java
class Solution {
    public int minimizeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;

        int m1 = nums[n - 3] - nums[0];
        int m2 = nums[n - 2] - nums[1];
        int m3 = nums[n - 1] - nums[2];

        return Math.min(m1, Math.min(m2, m3));
    }
}
