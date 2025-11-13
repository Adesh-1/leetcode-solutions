# 485. Max Consecutive Ones
# in python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for i in nums:
            if i == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

# in java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0, maxCount = 0;

        for (int i : nums) {
            if (i == 1) {
                count++;
                maxCount = Math.max(maxCount, count);
            } else {
                count = 0;
            }
        }

        return maxCount;
    }
}
