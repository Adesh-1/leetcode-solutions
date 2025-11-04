# 387. First Unique Character in a String
# in python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for key, val in d.items():
            if val == 1:
                return s.find(key)
        return -1

# in java
class Solution {
    public int firstUniqChar(String s) {
        int[] freq = new int[26];

        // Count frequency of each character
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        // Find first character with frequency 1
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
}
