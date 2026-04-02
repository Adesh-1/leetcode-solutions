# 2309. Greatest English Letter in Upper and Lower Case
# in python
class Solution:
    def greatestLetter(self, s: str) -> str:
        st = set(s)
        for ch in range(ord("Z"), ord("A") - 1, -1):
            upper = chr(ch)
            lower = chr(ch + 32)  # or upper.lower()

            if upper in st and lower in st:
                return upper
        return ""

# in java
class Solution {
    public String greatestLetter(String s) {
        for (int ch = 'z'; ch >= 'a'; ch--) {
            String lo = Character.toString(ch);
            String up = Character.toString(ch - 32);
            if (s.contains(up) && s.contains(lo))
                return up;
        }
        return "";
    }
}
