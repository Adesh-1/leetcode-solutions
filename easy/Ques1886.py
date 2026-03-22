# 1886. Determine Whether Matrix Can Be Obtained By Rotation
# in python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            # transpose
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # reverse each row
            for row in matrix:
                row.reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)

        return False

# in java
class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;

        boolean r0 = true, r90 = true, r180 = true, r270 = true;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                int val = mat[i][j];

                if (val != target[i][j])
                    r0 = false;

                if (val != target[j][n - 1 - i])
                    r90 = false;

                if (val != target[n - 1 - i][n - 1 - j])
                    r180 = false;

                if (val != target[n - 1 - j][i])
                    r270 = false;
            }
        }

        return r0 || r90 || r180 || r270;
    }
}
