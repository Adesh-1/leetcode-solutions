# 921. Minimum Add to Make Parentheses Valid
# in python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op, m = 0, 0
        for ch in s:
            if ch == "(":
                op += 1
            else:
                if op > 0:
                    op -= 1
                else:
                    m += 1
        return m + op

# in java
class Solution {
    public int minAddToMakeValid(String s) {
        int op = 0, m = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(')
                op++;
            else {
                if (op > 0)
                    op--;
                else
                    m++;
            }
        }
        return m + op;
    }
}
