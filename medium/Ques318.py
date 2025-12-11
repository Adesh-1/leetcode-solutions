# 318. Maximum Product of Word Lengths
# in python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        sets = [set(w) for w in words]

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if sets[i].isdisjoint(sets[j]):     # no common letter
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

# in java
class Solution {
    public int maxProduct(String[] words) {
        int n = words.length;
        int[] masks = new int[n];

        for (int i = 0; i < n; i++) {
            int mask = 0;
            for (char c : words[i].toCharArray()) {
                mask |= 1 << (c - 'a');
            }
            masks[i] = mask;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((masks[i] & masks[j]) == 0) {
                    ans = Math.max(ans, words[i].length() * words[j].length());
                }
            }
        }
        return ans;
    }
}
