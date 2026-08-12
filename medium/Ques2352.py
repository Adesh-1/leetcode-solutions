# 2352. Equal Row and Column Pairs
# in python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)

        return sum(rows[col] for col in zip(*grid))

# in java
class Solution {
    public int equalPairs(int[][] grid) {
        Map<List<Integer>, Integer> map = new HashMap<>();

        for (int[] row : grid) {
            List<Integer> list = new ArrayList<>();

            for (int num : row)
                list.add(num);

            map.put(list, map.getOrDefault(list, 0) + 1);
        }

        int ans = 0;

        for (int j = 0; j < grid.length; j++) {
            List<Integer> column = new ArrayList<>();

            for (int i = 0; i < grid.length; i++)
                column.add(grid[i][j]);

            ans += map.getOrDefault(column, 0);
        }

        return ans;
    }
}
