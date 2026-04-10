# 3740. Minimum Distance Between Three Equal Elements I
# in python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dis = abs(i - j) + abs(j - k) + abs(k - i)
                        ans = min(dis, ans)
        return -1 if ans == float("inf") else ans

# in java
class Solution {
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] == nums[j] && nums[j] == nums[k]) {
                        int dist = Math.abs(i - j) + Math.abs(j - k) + Math.abs(k - i);
                        ans = Math.min(dist, ans);
                    }
                }
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
