# 3736. Minimum Moves to Equal Array Elements III
# in python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)

# in java
class Solution {
    public int minMoves(int[] nums) {
        int max = nums[0];
        int sum = 0;

        for (int num : nums) {
            max = Math.max(max, num);
            sum += num;
        }

        return max * nums.length - sum;
    }
}
