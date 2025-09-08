// 54. Spiral Matrix
// in java
class Solution {
    public List<Integer> spiralOrder(int[][] mat) {
        List<Integer> l = new ArrayList<>();
        int m = mat.length;
        int n = mat[0].length;
        int srow = 0, erow = m - 1;
        int scol = 0, ecol = n - 1;
        while (scol <= ecol && srow <= erow) {
            // top
            for (int i = scol; i <= ecol; i++) {
                l.add(mat[srow][i]);
            }
            // right
            for (int i = srow + 1; i <= erow; i++) {
                l.add(mat[i][ecol]);
            }
            // bottom
            for (int i = ecol - 1; i >= scol; i--) {
                if (srow == erow)
                    break;
                l.add(mat[erow][i]);
            }
            // left
            for (int i = erow - 1; i >= srow + 1; i--) {
                if (scol == ecol)
                    break;
                l.add(mat[i][scol]);
            }
            srow++;
            scol++;
            erow--;
            ecol--;
        }
        return l;
    }
}


// in python
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        l = []
        m = len(mat)          # number of rows
        n = len(mat[0])       # number of columns
        srow, erow = 0, m - 1
        scol, ecol = 0, n - 1

        while scol <= ecol and srow <= erow:
            # top
            for i in range(scol, ecol + 1):
                l.append(mat[srow][i])
            
            # right
            for i in range(srow + 1, erow + 1):
                l.append(mat[i][ecol])
            
            # bottom
            for i in range(ecol - 1, scol - 1, -1):
                if srow == erow:
                    break
                l.append(mat[erow][i])
            
            # left
            for i in range(erow - 1, srow, -1):
                if scol == ecol:
                    break
                l.append(mat[i][scol])
            
            srow += 1
            scol += 1
            erow -= 1
            ecol -= 1
        
        return l
