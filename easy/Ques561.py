# 561. Array Partition
# in python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum

# in java
class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; i += 2)
            sum += nums[i];
        return sum;
    }
}
