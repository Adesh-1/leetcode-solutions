# 2592. Maximize Greatness of an Array
# in python
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        l = r = 0
        while r < len(nums):
            if nums[r] > nums[l]:
                l += 1
            r += 1
        return l

# in java
class Solution {
    public int maximizeGreatness(int[] nums) {
        Arrays.sort(nums);
        int l = 0, r = 0;
        while (r < nums.length) {
            if (nums[r] > nums[l])
                l++;
            r++;
        }
        return l;
    }
}
