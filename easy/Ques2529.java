// 2529. Maximum Count of Positive Integer and Negative Integer
// in java
class Solution {
    public int maximumCount(int[] nums) {
        int pos = 0, neg = 0;
        for (int val : nums) {
            if (val == 0) // skip this step, do nothing
                continue;
            else if (val > 0) // for count positive numbers
                pos++;
            else // for count negative numbers
                neg++;
        }
        return Math.max(pos, neg);
    }
}

// in pyhton
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        for val in nums:
            if val == 0:  # skip this step, do nothing
                continue
            elif val > 0:  # for count positive numbers
                pos += 1
            else:  # for count negative numbers
                neg += 1
        return max(pos, neg)
