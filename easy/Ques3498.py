# 3498. Reverse Degree of a String
# in python
class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s):
            ans += (123 - ord(ch)) * (i + 1)
        return ans

# in python
class Solution {
    public int reverseDegree(String s) {
        int ans = 0;
        int i = 1;

        for (char ch : s.toCharArray())
            ans += (123 - (int) ch) * i++;

        return ans;
    }
}
