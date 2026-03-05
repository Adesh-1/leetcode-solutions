# 1758. Minimum Changes To Make Alternating Binary String
# in python
class Solution:
    def minOperations(self, s: str) -> int:
        mismatch = 0
        for i in range(len(s)):
            expected = "0" if i % 2 == 0 else "1"
            if s[i] != expected:
                mismatch += 1
        return min(mismatch, len(s) - mismatch)

# in java
class Solution {
    public int minOperations(String s) {
        int mismatch = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char expected = (i % 2 == 0) ? '0' : '1';
            
            if (s.charAt(i) != expected) {
                mismatch++;
            }
        }
        
        return Math.min(mismatch, s.length() - mismatch);
    }
}
