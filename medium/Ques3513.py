# 3513. Number of Unique XOR Triplets I
# in python
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        return 1 << n.bit_length()

# in java
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        if (n < 3)
            return n;
        int bit = 32 - Integer.numberOfLeadingZeros(n);
        return 1 << bit;
    }
}
