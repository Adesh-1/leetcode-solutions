# 657. Robot Return to Origin
# in python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

# in java
        # 1st method
class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        for (char c : moves.toCharArray()) {
            if (c == 'U')
                y++;
            else if (c == 'D')
                y--;
            else if (c == 'L')
                x--;
            else if (c == 'R')
                x++;
        }
        return x == 0 && y == 0;
    }
}

        # 2nd method
class Solution {
    public boolean judgeCircle(String moves) {
        int[] ch = new int[26];
        for (char move : moves.toCharArray())
            ch[move - 'A']++;
        return ch['U' - 'A'] == ch['D' - 'A'] &&
                ch['L' - 'A'] == ch['R' - 'A'];
    }

}
