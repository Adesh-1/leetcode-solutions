# 2500. Delete Greatest Value in Each Row
# in python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        return sum(max(col) for col in zip(*grid))

# in java
class Solution {
    public int deleteGreatestValue(int[][] grid) {
        for (int[] row : grid)
            Arrays.sort(row);

        int ans = 0;
        for (int j = grid[0].length-1; j >= 0; j--) {
            int max = 0;
            for (int i = 0; i < grid.length; i++)
                max = Math.max(max, grid[i][j]);
            ans += max;
        }
        return ans;
    }
}
