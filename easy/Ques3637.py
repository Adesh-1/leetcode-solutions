# 3637. Trionic Array I
# in python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        # 1️⃣ strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == 1 or i == n:
            return False

        # 2️⃣ strictly decreasing
        while i < n and nums[i] < nums[i - 1]:
            i += 1
        if i == n:
            return False

        # 3️⃣ strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1

        return i == n

# in java
class Solution {
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        int i = 1;

        while (i < n && nums[i] > nums[i - 1])
            i++;
        if (i == 1 || i == n)
            return false;

        while (i < n && nums[i] < nums[i - 1])
            i++;
        if (i == n)
            return false;

        while (i < n && nums[i] > nums[i - 1])
            i++;

        return i==n;
    }
}
