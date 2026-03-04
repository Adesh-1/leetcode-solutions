# 1582. Special Positions in a Binary Matrix
# in python
class Solution:
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        # Step 1: Count 1's in rows and columns
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        count = 0
        
        # Step 2: Check special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    count += 1
        
        return count

# in java
class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        int[] row_count = new int[m];
        int[] col_count = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    row_count[i]++;
                    col_count[j]++;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && row_count[i] == 1 && col_count[j] == 1)
                    count++;
            }
        }

        return count;
    }
}
