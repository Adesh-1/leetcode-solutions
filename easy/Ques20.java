// 20. Valid Parentheses
// in pyhton
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            match ch:
                case '(' | '{' | '[':
                    stack.append(ch)
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False

        return not stack

    // in java
    class Solution {
    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int top = -1;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            // Push opening brackets
            if (ch == '(' || ch == '{' || ch == '[') {
                stack[++top] = ch;
            } 
            // Check closing brackets
            else if (top == -1 || 
                     (ch == ')' && stack[top] != '(') || 
                     (ch == '}' && stack[top] != '{') || 
                     (ch == ']' && stack[top] != '[')) {
                return false;
            } else {
                top--; // pop if matched
            }
        }

        return top == -1;
    }
}
