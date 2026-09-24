# 3550. Smallest Index With Digit Sum Equal to Index
# in python
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(map(int, str(num))) == i:
                return i

        return -1

# in java
class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;

            while (nums[i] != 0) {
                sum += nums[i] % 10;
                nums[i] /= 10;
            }

            if (sum == i)
                return i;
        }
        return -1;
    }
}
