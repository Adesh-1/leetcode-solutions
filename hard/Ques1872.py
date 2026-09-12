# 1872. Stone Game VIII
# in python
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        dp = stones[-1]
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, stones[i] - dp)

        return dp

# in java
class Solution {
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        for (int i = 1; i < n; i++)
            stones[i] += stones[i - 1];

        int dp = stones[n - 1];
        for (int i = n - 2; i > 0; i--)
            dp = Math.max(dp, stones[i] - dp);

        return dp;
    }
}
