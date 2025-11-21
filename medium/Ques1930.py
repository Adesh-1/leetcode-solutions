# 1930. Unique Length-3 Palindromic Subsequences
# in python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for code in range(ord("a"), ord("z") + 1):
            ch = chr(code)
            l = s.find(ch)
            r = s.rfind(ch)
            if l != -1 and l < r:
                res += len(set(s[l + 1 : r]))
        return res
