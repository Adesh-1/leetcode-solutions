# 2390. Removing Stars From a String
# in python
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

# in java
class Solution {
    public String removeStars(String s) {
        StringBuilder sb = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (ch == '*')
                sb.deleteCharAt(sb.length() - 1);
            else
                sb.append(ch);
        }

        return sb.toString();
    }
}
