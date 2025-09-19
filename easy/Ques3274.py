# 3274. Check if Two Chessboard Squares Have the Same Color
# in python
class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        a1, b1 = ord(c1[0]) - 96, int(c1[1]) # we can use ord('a')+1 in place or 96
        a2, b2 = ord(c2[0]) - 96, int(c2[1])
        return (a1 + b1) % 2 == (a2 + b2) % 2

  # in java
  class Solution {
    public boolean checkTwoChessboards(String c1, String c2) {
        int a1 = c1.charAt(0) - 'a' + 1;
        int b1 = c1.charAt(1) - '0';

        int a2 = c2.charAt(0) - 'a' + 1;
        int b2 = c2.charAt(1) - '0';
        
        return (a1 + b1) % 2 == (a2 + b2) % 2;
    }
}
