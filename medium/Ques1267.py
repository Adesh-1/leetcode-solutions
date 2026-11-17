# 1267. Count Servers that Communicate
# in python
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row = [0] * m
        col = [0] * n

        # Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        count = 0

        # Count communicating servers
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    count += 1

        return count

# in java
class Solution {
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[] row = new int[m];
        int[] col = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    row[i]++;
                    col[j]++;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (row[i] > 1 || col[j] > 1)) {
                    count++;
                }
            }
        }

        return count;

    }
}
