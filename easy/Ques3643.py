# 3643. Flip Square Submatrix Vertically
# in python
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            for j in range(y, y + k):
                # swap elements row-wise
                grid[x + i][j], grid[x + k - 1 - i][j] = grid[x + k - 1 - i][j], grid[x + i][j]
        
        return grid

# in java
class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        for (int i = 0; i < k / 2; i++) {
            for (int j = y; j < y + k; j++) {

                int temp = grid[x + i][j];
                grid[x + i][j] = grid[x + k - 1 - i][j];
                grid[x + k - 1 - i][j] = temp;
            }
        }

        return grid;
    }
}
