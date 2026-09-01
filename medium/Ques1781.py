# 1781. Sum of Beauty of All Substrings
# in python
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - ord("a")] += 1

                max_freq = max(freq)
                min_freq = min(x for x in freq if x > 0)

                ans += max_freq - min_freq

        return ans

# in java
class Solution {
    public int beautySum(String s) {
        int ans = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];

            for (int j = i; j < n; j++) {
                freq[s.charAt(j) - 'a']++;

                int maxFreq = Integer.MIN_VALUE;
                int minFreq = Integer.MAX_VALUE;

                for (int x : freq) {
                    maxFreq = Math.max(maxFreq, x);

                    if (x > 0)
                        minFreq = Math.min(minFreq, x);
                }

                ans += (maxFreq - minFreq);
            }
        }
        return ans;
    }
}
