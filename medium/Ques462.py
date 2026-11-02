# 462. Minimum Moves to Equal Array Elements II
# in python
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()

        median = nums[len(nums) // 2]

        return sum(abs(num - median) for num in nums)

# in java
class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);

        int median = nums[nums.length / 2];

        int moves = 0;
        for (int num : nums)
            moves += Math.abs(num - median);

        return moves;
    }
}
