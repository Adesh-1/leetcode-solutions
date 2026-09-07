# 940. Distinct Subsequences II
# in python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007
        dp = 1
        last = [0] * 26

        for i in range(len(s)):
            ind = ord(s[i]) - ord("a")
            newDP = (2 * dp - last[ind] + MOD) % MOD

            last[ind] = dp
            dp = newDP

        return (dp - 1 + MOD) % MOD

# in java
class Solution {
    public int distinctSubseqII(String s) {
        long MOD = 1000000007;

        long dp = 1;
        long[] last = new long[26];

        for (char ch : s.toCharArray()) {
            int index = ch - 'a';

            long newDp = (2 * dp - last[index] + MOD) % MOD;

            last[index] = dp;
            dp = newDp;
        }

        return (int) ((dp - 1 + MOD) % MOD);
    }
}
