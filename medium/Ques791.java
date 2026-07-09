// 791. Custom Sort String
// in python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []

        for ch in order:
            ans.append(ch * count[ch])
            count[ch] = 0

        for ch in count:
            ans.append(ch * count[ch])

        return "".join(ans)

// in java
  class Solution {
    public String customSortString(String order, String s) {
        int[] freq = new int[26];

        // Count frequency of each character in s
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }

        StringBuilder ans = new StringBuilder();

        // Append characters according to order
        for (char ch : order.toCharArray()) {
            while (freq[ch - 'a'] > 0) {
                ans.append(ch);
                freq[ch - 'a']--;
            }
        }

        // Append remaining characters
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                ans.append((char) (i + 'a'));
                freq[i]--;
            }
        }

        return ans.toString();
    }
}
