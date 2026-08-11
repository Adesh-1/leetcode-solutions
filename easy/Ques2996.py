# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
# in python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sum += nums[i]
            else:
                break

        s = set(nums)
        while sum in s:
            sum += 1

        return sum

# in java
class Solution {
    public int missingInteger(int[] nums) {
        int sum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1)
                sum += nums[i];
            else
                break;
        }

        Set<Integer> set = new HashSet<>();
        for (int num : nums)
            set.add(num);

        while (set.contains(sum))
            sum++;

        return sum;
    }
}
