# 3713. Longest Balanced Substring I
      # same as 3719. Longest Balanced Subarray I
# in pyhton
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = {}          # like even/odd sets
            max_freq = 0

            for j in range(i, n):
                ch = s[j]

                # update frequency
                freq[ch] = freq.get(ch, 0) + 1

                # update max frequency
                max_freq = max(max_freq, freq[ch])

                distinct = len(freq)
                length = j - i + 1

                # balanced condition
                if max_freq * distinct == length:
                    ans = max(ans, length)

        return ans

# in java
class Solution {
    public int longestBalanced(String s) {
        int n = s.length();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int[] freq = new int[26]; # // frequency array
            int maxFreq = 0;
            int distinct = 0;

            for (int j = i; j < n; j++) {
                char ch = s.charAt(j);
                int index = ch - 'a';

                # // if first time appearing
                if (freq[index] == 0) {
                    distinct++;
                }

                freq[index]++;
                maxFreq = Math.max(maxFreq, freq[index]);

                int length = j - i + 1;

                # // check balanced condition
                if (maxFreq * distinct == length) {
                    ans = Math.max(ans, length);
                }
            }
        }

        return ans;
    }
}
