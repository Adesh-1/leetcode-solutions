# 3090. Maximum Length Substring With Two Occurrences
# in python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = Counter()
        left = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans

# in java
class Solution {
    public int maximumLengthSubstring(String s) {
        int[] freq = new int[26];
        int left = 0;
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {
            freq[s.charAt(right) - 'a']++;

            while (freq[s.charAt(right) - 'a'] > 2) {
                freq[s.charAt(left) - 'a']--;
                left++;
            }

            ans = Math.max(ans, right - left + 1);
        }

        return ans;
    }
}
