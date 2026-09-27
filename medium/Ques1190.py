# 1190. Reverse Substrings Between Each Pair of Parentheses
# in python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""

        for ch in s:
            if ch == "(":
                stack.append(current)
                current = ""

            elif ch == ")":
                current = stack.pop() + current[::-1]

            else:
                current += ch

        return current

# in java
class Solution {
    public String reverseParentheses(String s) {
        Stack<String> stack = new Stack<>();
        StringBuilder current = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                stack.push(current.toString());
                current.setLength(0);
            }

            else if (ch == ')') {
                current.reverse();
                current.insert(0, stack.pop());
            }

            else
                current.append(ch);
        }
        return current.toString();
    }
}
