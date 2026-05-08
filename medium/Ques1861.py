# 1861. Rotating the Box
# in python
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for i in range(m):
            empty_pos = n - 1

            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    empty_pos = j - 1

                elif boxGrid[i][j] == "#":
                    boxGrid[i][j], boxGrid[i][empty_pos] = (
                        boxGrid[i][empty_pos],
                        boxGrid[i][j],
                    )
                    empty_pos -= 1

        res = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        return res

# in java
class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {
        int m = boxGrid.length;
        int n = boxGrid[0].length;

        for (int i = 0; i < m; i++) {

            int emptyPos = n - 1;

            for (int j = n - 1; j >= 0; j--) {

                if (boxGrid[i][j] == '*') {
                    emptyPos = j - 1;
                }

                else if (boxGrid[i][j] == '#') {

                    char temp = boxGrid[i][emptyPos];
                    boxGrid[i][emptyPos] = '#';
                    boxGrid[i][j] = temp;

                    emptyPos--;
                }
            }
        }

        char[][] res = new char[n][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        return res;

    }
}
