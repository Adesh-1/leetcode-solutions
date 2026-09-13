# 1909. Remove One Element to Make the Array Strictly Increasing
# in python
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = v = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                count += 1
                v = i

        if count > 1:
            return False
        elif count == 1:
            if v == 0 or v == len(nums) - 2:
                return True
            elif nums[v - 1] < nums[v + 1] or nums[v] < nums[v + 2]:
                return True
            else:
                return False

        return True

# in java
class Solution {
    public boolean canBeIncreasing(int[] nums) {
        int count = 0;
        int v = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] >= nums[i + 1]) {
                count++;
                v = i;
            }
        }

        if (count > 1)
            return false;
        else if (count == 1) {
            if (v == 0 || v == nums.length - 2)
                return true;
            else if (nums[v - 1] < nums[v + 1] || nums[v] < nums[v + 2])
                return true;
            else
                return false;
        }

        return true;
    }
}
