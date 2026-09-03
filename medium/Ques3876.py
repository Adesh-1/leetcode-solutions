# 3876. Construct Uniform Parity Array II
# in python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m = min(nums1)

        # If the minimum number is odd, every other number can be made odd
        if m & 1:  # or can be written as 'm % 2 == 1'
            return True

        # If the minimum is even, an odd number would make the array non-uniform
        for i in nums1:
            if i & 1:
                return False

        return True

# in java
class Solution {
    public boolean uniformArray(int[] nums1) {
        int min = Integer.MAX_VALUE;
        for (int i : nums1)
            min = Math.min(min, i);

        if (min % 2 == 1)
            return true;

        for (int n : nums1)
            if (n % 2 == 1)
                return false;

        return true;
    }
}
