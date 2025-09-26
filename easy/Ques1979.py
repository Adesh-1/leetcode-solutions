# 1979. Find Greatest Common Divisor of Array
# in python
import math as m


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return m.gcd(min(nums), max(nums))

  # in java
  class Solution {
    public int findGCD(int[] nums) {
        Arrays.sort(nums);
        int a = nums[0];
        int b = nums[nums.length - 1];
        while (b != 0) {
            int temp = a;
            a = b;
            b = temp % b;
        }
        return a;
    }
}
