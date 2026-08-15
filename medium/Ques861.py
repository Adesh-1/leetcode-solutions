# 861. Score After Flipping Matrix
# in python
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Make the first column all 1s
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        score = 0

        # Optimize every column
        for j in range(n):
            ones = 0

            for i in range(m):
                ones += grid[i][j]

            zeros = m - ones

            # Maximum possible 1s in this column
            best = max(ones, zeros)

            # Value of this binary position
            value = 1 << (n - 1 - j)

            score += best * value

        return score


# in java (same as python)
class Solution {
    public int matrixScore(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                for (int j = 0; j < n; j++)
                    grid[i][j] ^= 1;
            }
        }

        int score = 0;
        for (int j = 0; j < n; j++) {
            int ones = 0;
            for (int i = 0; i < m; i++) {
                if (grid[i][j] == 1)
                    ones++;
            }
            int zeros = m - ones;
            int best = Math.max(ones, zeros);
            int value = 1 << (n - 1 - j);
            score += best * value;
        }
        return score;
    }
}
