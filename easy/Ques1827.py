# 1827. Minimum Operations to Make the Array Increasing
# in python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        previous_number = nums[0]
        result = 0

        for i in range(1, len(nums)):
            previous_number = max(previous_number + 1, nums[i])
            result += previous_number - nums[i]
            
        return result

# in java
class Solution {
    public int minOperations(int[] nums) {
        int oprs = 0;

        for (int i = 1; i < nums.length; i++) {

            if (nums[i] <= nums[i - 1]) {
                int need = nums[i - 1] + 1;
                oprs += need - nums[i];
                nums[i] = need;
            }

        }
        return oprs;
    }
}
