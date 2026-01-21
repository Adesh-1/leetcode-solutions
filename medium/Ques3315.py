# 3315. Construct the Minimum Bitwise Array II

# in python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n & (n - 1) == 0:
                ans.append(-1)
            else:
                mask = 1
                while n & mask:
                    mask <<= 1
                ans.append(n - (mask >> 1))
        return ans

# in java
class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            int num = nums.get(i);

            if ((num & (num - 1)) == 0) { # // power of 2 → impossible
                ans[i] = -1;
            } else {
                int mask = 1;
                while ((num & mask) != 0) {
                    mask <<= 1; # // skip trailing 1s
                }
                ans[i] = num - (mask >> 1); # // remove last 1 in trailing 1s
            }
        }

        return ans;
    }
}
