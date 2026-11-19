# 3364. Minimum Positive Sum Subarray 
# in python
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float("inf")
        n = len(nums)

        for i in range(n):
            s = 0

            for j in range(i, n):
                s += nums[j]  # add each value for each subarray

                # Check if the subarray length is within [l, r]
                length = j - i + 1

                if l <= length <= r:  # check length
                    if s > 0:
                        ans = min(ans, s)

        if ans == float("inf"):
            return -1            
        return ans

# in java
class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int ans = Integer.MAX_VALUE;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int sum = 0;

            for (int j = i; j < n; j++) {
                sum += nums.get(j);

                int len = j - i + 1;
                if (len >= l && len <= r)
                    if (sum > 0)
                        ans = Math.min(ans, sum);
            }
        }

        if (ans == Integer.MAX_VALUE)
            return -1;
        return ans;
    }
}
