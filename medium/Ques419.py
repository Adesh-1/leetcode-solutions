# 419. Battleships in a Board
# in python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        m,n=len(board),len(board[0])
        count =0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    # check above and left
                    if(i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                        count+=1
        return count

# in java
class Solution {
    public int countBattleships(char[][] board) {
        if (board == null || board.length == 0)
            return 0;
        int m = board.length;
        int n = board[0].length;
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'X') {
                    if ((i == 0 || board[i - 1][j] == '.') && (j == 0 || board[i][j - 1] == '.'))
                        count++;
                }
            }
        }
        return count;
    }
}
