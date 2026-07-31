// 3016. Minimum Number of Pushes to Type Word II
// in python
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        ans = 0
        for i, f in enumerate(freq):
            ans += ((i // 8) + 1) * f
        return ans

// in java
class Solution {
    public int minimumPushes(String word) {
        int[] freq = new int[26];

        // Count frequency of each character
        for (char ch : word.toCharArray()) {
            freq[ch - 'a']++;
        }

        // Sort frequencies in ascending order
        Arrays.sort(freq);

        int pushes = 1;
        int count = 0;
        int ans = 0;

        // Traverse from largest frequency to smallest
        for (int i = 25; i >= 0; i--) {
            if (freq[i] == 0) break;

            ans += freq[i] * pushes;
            count++;

            // After every 8 letters, increase the push count
            if (count % 8 == 0) {
                pushes++;
            }
        }

        return ans;
    }
}
