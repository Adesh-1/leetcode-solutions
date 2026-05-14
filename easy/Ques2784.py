# 2784. Check if Array is Good
# in python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) != m + 1:
            return False

        c = Counter(nums)
        for i in range(1, m):
            if c[i] != 1:
                return False

        return c[m] == 2

# in java
class Solution {
    public boolean isGood(int[] nums) {
        int m = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (m < nums[i])
                m = nums[i];
        }

        if (nums.length != m + 1)
            return false;

        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums)
            count.put(num, count.getOrDefault(num, 0) + 1);

        for (int i = 1; i < m; i++) {
            if (count.getOrDefault(i, 0) != 1)
                return false;
        }

        return count.getOrDefault(m, 0) == 2;
    }
}
