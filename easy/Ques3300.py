# 3300. Minimum Element After Replacement With Digit Sum
# in python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = float("inf")
        for i in nums:
            sum = 0
            while i != 0:
                sum += i % 10
                i //= 10
            min_val = min(min_val, sum)
        return min_val

# in java
class Solution {
    public int minElement(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int i : nums) {
            int sum = 0;
            while (i != 0) {
                sum += i % 10;
                i /= 10;
            }
            min = Math.min(min, sum);
        }
        return min;
    }
}
