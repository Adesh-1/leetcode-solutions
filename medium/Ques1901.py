# 1901. Find a Peak Element II
# in python
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        val = 0
        l = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] > val:
                    val = mat[i][j]
                    l.append([i, j])
        return l[-1]

# in java
class Solution {
    public int[] findPeakGrid(int[][] mat) {
        int maxVal = Integer.MIN_VALUE;
        int[] pos = new int[2];

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] > maxVal) {
                    maxVal = mat[i][j];
                    pos[0] = i;
                    pos[1] = j;
                }
            }
        }

        return pos;
    }
}
