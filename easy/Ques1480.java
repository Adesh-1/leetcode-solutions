// 1480. Running Sum of 1d Array
// in java
class Solution {
    public int[] runningSum(int[] nums) {
        for(int i = 1; i < nums.length; i++)
            nums[i] += nums[i-1];
        return nums;
    }
}

// in python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        n = 0
        for i in range(0,len(nums)):
            n += nums[i]
            l.append(n)
        return l
