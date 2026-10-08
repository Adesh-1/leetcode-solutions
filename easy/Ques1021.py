# 1021. Remove Outermost Parentheses
# in python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, depth = [], 0

        for ch in s:
            if ch == "(":
                if depth > 0:
                    ans.append(ch)
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    ans.append(ch)

        return "".join(ans)

# in java
class Solution {
    public static String removeOuterParentheses(String s) {
        StringBuilder ans = new StringBuilder();
        int depth = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                if (depth > 0)
                    ans.append(ch);
                depth++;
            }

            else {
                depth--;
                if (depth > 0)
                    ans.append(ch);
            }
        }
        return ans.toString();
    }
}
