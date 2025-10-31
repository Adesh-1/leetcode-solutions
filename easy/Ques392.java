// 392. Is Subsequence
// in java
class Solution {
    public boolean isSubsequence(String s, String t) {
        for (char c : s.toCharArray()) {
            int idx = t.indexOf(c);
            if (idx == -1) {      // character not found
                return false;
            }
            t = t.substring(idx + 1); // cut t after found character
        }
        return true;
    }
}

// in python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
