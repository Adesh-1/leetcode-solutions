# 32. Longest Valid Parentheses
# in python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans

# in java
class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> st = new Stack<>();
        st.push(-1);

        int ans = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(')
                st.push(i);
            else {
                st.pop();

                if (st.isEmpty())
                    st.push(i);
                else
                    ans = Math.max(ans, i - st.peek());
            }
        }
        return ans;
    }
}
