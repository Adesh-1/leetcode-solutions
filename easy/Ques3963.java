// 3963. Create Grid With Exactly One Path
// in python
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        for i in range(m):
            row = ['#'] * n

            if i == 0:
                row = ['.'] * n

            row[n - 1] = '.'

            grid.append(''.join(row))

        return grid

// in java
class Solution {
    public String[] createGrid(int m, int n) {
        String[] grid = new String[m];

        for (int i = 0; i < m; i++) {
            // Create a row of size n
            char[] row = new char[n];

            // Fill the entire row with obstacles
            Arrays.fill(row, '#');

            // Make the first row completely free
            if (i == 0)
                Arrays.fill(row, '.');

            // Make the last column free
            row[n - 1] = '.';

            // Convert the character array into a String
            grid[i] = new String(row);
        }

        return grid;
    }
}
