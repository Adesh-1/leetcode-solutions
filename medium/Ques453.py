# 453. Minimum Moves to Equal Array Elements
# in python
    # 1st method
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minVal = min(nums)
        return sum(num - minVal for num in nums)

    # 2nd method
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

# in java
class Solution {
    public int minMoves(int[] nums) {
        int min = nums[0];
        int sum = 0;

        for (int num : nums) {
            min = Math.min(min, num);
            sum += num;
        }

        return sum - (min * nums.length);
    }
}
