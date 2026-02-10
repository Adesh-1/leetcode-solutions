# 3719. Longest Balanced Subarray I
# in python
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            even = set()
            odd = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(even) == len(odd):
                    ans = max(ans, j - i + 1)
        return ans

# for more information follow below link -->
# https://chatgpt.com/share/698b6ba6-7528-800c-a014-13d22ec6deb5

# in java
class Solution {
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            Set<Integer> even = new HashSet<>();
            Set<Integer> odd = new HashSet<>();

            for (int j = i; j < n; j++) {
                if (nums[j] % 2 == 0)
                    even.add(nums[j]);
                else
                    odd.add(nums[j]);

                if (even.size() == odd.size())
                    ans = Math.max(ans, j - i + 1);
            }
        }
        return ans;
    }
}
