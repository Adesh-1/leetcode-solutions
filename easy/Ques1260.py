# 1260. Shift 2D Grid
# in python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ind = i * n + j
                newInd = (ind + k) % total
                newRow = newInd // n
                newCol = newInd % n

                ans[newRow][newCol] = grid[i][j]
        return ans

# in java
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;

        int total = m * n;
        k %= total;

        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(0);
            }
            ans.add(row);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int idx = i * n + j;
                int newIdx = (idx + k) % total;

                int newRow = newIdx / n;
                int newCol = newIdx % n;

                ans.get(newRow).set(newCol, grid[i][j]);
            }
        }

        return ans;
    }
}
