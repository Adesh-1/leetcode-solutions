# 3467. Transform Array by Parity
# in python
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([0 if i % 2 == 0 else 1 for i in nums])

  # or (simple to understand)
  class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            val = 0 if i % 2 == 0 else 1
            res.append(val)
        return sorted(res)

# in java
class Solution {
    public int[] transformArray(int[] nums) {
        int[] parity_arr = new int[nums.length]; // by default all values are 0
        int ind = nums.length - 1;
        for (int n : nums) {
            if (n % 2 != 0)
                parity_arr[ind--] = 1;
        }
        return parity_arr;
    }
}

# or (simple to understand)
class Solution {
    public int[] transformArray(int[] nums) {
        int[] parity_arr = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
            parity_arr[i] = nums[i] % 2 == 0 ? 0 : 1;
        Arrays.sort(parity_arr);
        return parity_arr;
    }
}
