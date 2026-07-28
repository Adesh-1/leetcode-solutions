# 3517. Smallest Palindromic Rearrangement I
# in python
    # tricky solution
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = len(s)
        half = l // 2

        left = "".join(sorted(s[:half]))
        right = left[::-1]

        if l % 2 == 1:
            return left + s[half] + right

        return left + right


    # optimized solution
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        left = []
        middle = ""

        for i in range(26):
            left.append(chr(i + ord("a")) * (freq[i] // 2))

            if freq[i] % 2:
                middle = chr(i + ord("a"))

        left = "".join(left)

        return left + middle + left[::-1]
