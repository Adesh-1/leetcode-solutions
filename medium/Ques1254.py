# 1254. Number of Closed Islands
# in python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # If we go outside the grid, the island is open
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Water does not make the island open
            if grid[r][c] == 1:
                return True

            # Mark land as visited
            grid[r][c] = 1

            # Explore all four directions
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up and down and left and right

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count

# in java
class Solution {
    public int closedIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int count = 0;

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 0)
                    if (dfs(grid, r, c, rows, cols))
                        count++;

        return count;
    }

    private boolean dfs(int[][] grid, int r, int c, int rows, int cols) {
        # base case 1
        if (r < 0 || r >= rows || c < 0 || c >= cols)
            return false;

        # base case 2
        if (grid[r][c] == 1)
            return true;

        grid[r][c] = 1;

        boolean up = dfs(grid, r - 1, c, rows, cols);
        boolean down = dfs(grid, r + 1, c, rows, cols);
        boolean left = dfs(grid, r, c - 1, rows, cols);
        boolean right = dfs(grid, r, c + 1, rows, cols);

        return up && down && left && right;
    }
}
