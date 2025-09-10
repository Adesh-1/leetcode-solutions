// 59. Spiral Matrix II
// in java
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] spm = new int[n][n];
        int srow = 0, scol = 0;
        int erow = n - 1, ecol = n - 1;
        int ele = 1;
        while (srow <= erow) {
            // top
            for (int i = scol; i <= ecol; i++) {
                spm[srow][i] = ele++;
            }
            // right
            for (int i = srow + 1; i <= erow; i++) {
                spm[i][ecol] = ele++;
            }
            // bottom
            for (int i = ecol - 1; i >= scol; i--) {
                if (srow == erow)
                    break;
                spm[erow][i] = ele++;
            }
            // left
            for (int i = erow - 1; i >= srow + 1; i--) {
                if (scol == ecol)
                    break;
                spm[i][scol] = ele++;
            }
            srow++;
            scol++;
            erow--;
            ecol--;
        }
        return spm;
    }
}


// in python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spm = [[0] * n for _ in range(n)]
        srow, scol = 0, 0
        erow, ecol = n - 1, n - 1
        ele = 1

        while srow <= erow:
            # top
            for i in range(scol, ecol + 1):
                spm[srow][i] = ele
                ele += 1

            # right
            for i in range(srow + 1, erow + 1):
                spm[i][ecol] = ele
                ele += 1

            # bottom
            for i in range(ecol - 1, scol - 1, -1):
                if srow == erow:
                    break
                spm[erow][i] = ele
                ele += 1

            # left
            for i in range(erow - 1, srow, -1):
                if scol == ecol:
                    break
                spm[i][scol] = ele
                ele += 1

            srow += 1
            scol += 1
            erow -= 1
            ecol -= 1

        return spm
