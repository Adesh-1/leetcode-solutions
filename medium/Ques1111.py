# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# in python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []

        for ch in seq:
            if ch == "(":
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1

        return ans

# in java
class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int depth = 0;
        int[] ans = new int[seq.length()];
        int i = 0;

        for (char ch : seq.toCharArray()) {
            if (ch == '(') {
                depth++;
                ans[i] = depth % 2;
            } else {
                ans[i] = depth % 2;
                depth--;
            }
            i++;
        }
        return ans;
    }
}
