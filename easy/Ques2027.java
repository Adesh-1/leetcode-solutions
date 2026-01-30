// 2027. Minimum Moves to Convert String
// in java
class Solution {
    public int minimumMoves(String s) {
        int c = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'X') {
                c++;
                i += 2; // for-loop will add +1 more → total skip = 3
            }
        }
        return c;
    }
}

// in python
class Solution:
    def minimumMoves(self, s: str) -> int:
        c = i = 0
        while i < len(s):
            if s[i] == "X":
                c += 1
                i += 3
            else:
                i += 1
        return c
