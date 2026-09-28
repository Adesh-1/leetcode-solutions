# 1614. Maximum Nesting Depth of the Parentheses
# in python
class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate((ch == "(") - (ch == ")") for ch in s))

# in java
class Solution {
    public int maxDepth(String s) {
        int depth = 0, ans = 0;
        for (char ch : s.toCharArray()) {
            depth += ch == '(' ? 1 : ch == ')' ? -1 : 0;
            ans = Math.max(ans, depth);
        }
        return ans;
    }
}
