// 1252. Cells with Odd Values in a Matrix
// in java
class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[][] a = new int[m][n];  // matrix banaya (default values = 0)

        for (int[] index : indices) {
            int r = index[0];
            int c = index[1];

            for (int j = 0; j < n; j++) // for updating row
                a[r][j]++;

            for (int i = 0; i < m; i++) // for updating column
                a[i][c]++;
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] % 2 == 1)
                    count++;
            }
        }
        return count;
    }
}

// for more info 
// https://chatgpt.com/share/68a75730-94c8-8001-9ed9-8f9f0cc0cdb8
