# 3432. Count Partitions with Even Sum Difference
# in python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 2 == 1:
            return 0
        return len(nums) - 1

# in java
class Solution {
    public int countPartitions(int[] nums) {
        int total = 0;
        for (int i : nums)
            total += i;
        if (total % 2 == 1)
            return 0;
        return nums.length - 1;
    }
}
