# 3190. Find Minimum Operations to Make All Elements Divisible by Three
# in python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # In Python, True = 1, False = 0
        return sum(i % 3 != 0 for i in nums)

# in java
class Solution {
    public int minimumOperations(int[] nums) {
        int c = 0;
        for (int i : nums) {
            if (i % 3 != 0)
                c++;
        }
        return c;
    }
}
