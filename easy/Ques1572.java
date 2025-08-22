// 1572. Matrix Diagonal Sum
// in java
class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j || i + j == n - 1)
                    sum += mat[i][j];
            }
        }
        return sum;
    }
}

// in python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    sum += mat[i][j]
        return sum
