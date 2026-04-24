# 2833. Furthest Point From Origin
# in python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        m, n = moves.count('L'), moves.count('R')
        return moves.count('_') + abs(m - n)

# in java
class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int l = 0, r = 0, x = 0;
        for (char ch : moves.toCharArray()) {
            if (ch == 'L')
                l++;
            else if (ch == 'R')
                r++;
            else
                x++;
        }
        return x + (Math.max(l, r) - Math.min(l, r));
    }
}
