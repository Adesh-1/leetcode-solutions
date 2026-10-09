# 1541. Minimum Insertions to Balance a Parentheses String
# in python
class Solution:
    def minInsertions(self, s: str) -> int:
        insertion = need = 0

        for ch in s:
            if ch == "(":
                if need % 2:
                    insertion += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    insertion += 1
                    need = 1

        return insertion + need

# in java
class Solution {
    public int minInsertions(String s) {
        int insertion = 0;
        int need = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                if (need % 2 != 0) {
                    insertion++;
                    need--;
                }
                need += 2;
            } else {
                need--;
                if (need < 0) {
                    insertion++;
                    need = 1;
                }
            }
        }
        return insertion + need;
    }
}
