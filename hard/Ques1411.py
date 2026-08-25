# 1411. Number of Ways to Paint N × 3 Grid
# in python
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        x = y = 6

        for i in range(2, n + 1):
            new_x = (3 * x + 2 * y) % MOD
            new_y = (2 * x + 2 * y) % MOD
            x, y = new_x, new_y

        return (x + y) % MOD

# in java
class Solution {
    public int numOfWays(int n) {
        final int MOD = 1000000007;
        long x = 6, y = 6;

        for (int i = 2; i <= n; i++) {
            long newX = (3 * x + 2 * y) % MOD;
            long newY = (2 * x + 2 * y) % MOD;
            x = newX;
            y = newY;
        }

        return (int) (x + y) % MOD;
    }
}
