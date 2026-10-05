# 856. Score of Parentheses
# in python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        count = 0

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                x = stack.pop()

                if x == 0:
                    x = 1
                else:
                    x *= 2    # x = 2 * x

                stack[-1] += x

        return stack[0]

# in java
class Solution {
    public int scoreOfParentheses(String s) {
        Stack<Integer> st = new Stack<>();
        st.push(0);

        for (char ch : s.toCharArray()) {
            if (ch == '(')
                st.push(0);
            else {
                int x = st.pop();

                if (x == 0)
                    x = 1;
                else
                    x *= 2;

                st.push(st.pop() + x);
            }
        }
        return st.pop();
    }
}
