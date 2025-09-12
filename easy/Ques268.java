// 268. Missing Number
// in java
class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        int sum = 0;
        for (int i = 0; i < len + 1; i++) {
            sum+=i;
        }
        int arrSum = Arrays.stream(nums).sum();
        return sum-arrSum;
    }
}

// in python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2   # sum of 0..n
        return total - sum(nums)

  // in python (simple idea) but time complexity O(n^2)
  class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
