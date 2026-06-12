# 22. Generate Parentheses
# in python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans

# in java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    private void backtrack(List<String> ans, String curr,
            int open, int close, int n) {

        if (curr.length() == 2 * n) {
            ans.add(curr);
            return;
        }

        if (open < n) {
            backtrack(ans, curr + "(", open + 1, close, n);
        }

        if (close < open) {
            backtrack(ans, curr + ")", open, close + 1, n);
        }
    }
}
