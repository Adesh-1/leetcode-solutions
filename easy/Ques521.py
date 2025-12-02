# 521. Longest Uncommon Subsequence I
# in python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))

# in java
class Solution {
    public int findLUSlength(String a, String b) {
        if (a.equals(b))
            return -1;
        return Math.max(a.length(), b.length());
    }
}
