# 80. Remove Duplicates from Sorted Array II
# in python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        for i in s:
            while nums.count(i) > 2:
                nums.remove(i)
        return len(nums)

# in java
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int i : nums) {
            if (k < 2 || i != nums[k - 2]) {
                nums[k] = i;
                k++;
            }
        }
        return k;
    }
}
