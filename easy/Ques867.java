// 867. Transpose Matrix
// in java
class Solution {
    public int[][] transpose(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] transpose = new int[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                transpose[j][i] = matrix[i][j];
        }
        return transpose;
    }
}

// in py
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transpose = [[0] * m for _ in range(n)]  # create n rows, each with m columns
        for i in range(m):
            for j in range(n):
                transpose[j][i] = matrix[i][j]
        return transpose

// for more info in py as like '[[0] * m for _ in range(n)] what this line do' follow this link
  // https://chatgpt.com/share/68b066b4-9240-8001-94a9-b10bd1d292aa  
