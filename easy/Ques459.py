# 459. Repeated Substring Pattern
# in python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

# in java
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        if (s == null || s.isEmpty())
            return false;
        String ss = (s + s).substring(1, 2 * s.length() - 1);
        return ss.contains(s);
    }
}
