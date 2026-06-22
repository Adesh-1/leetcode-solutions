// 1189. Maximum Number of Balloons
// in python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        return min(c["b"], c["a"], c["l"] // 2, c["o"] // 2, c["n"])

// in java
class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] freq = new int[26];
        
        // Count frequency of each character
        for (char ch : text.toCharArray())
            freq[ch - 'a']++;

        // Find the limiting character
        return Math.min(
                Math.min(freq['b' - 'a'], freq['a' - 'a']),
                Math.min(
                        Math.min(freq['l' - 'a'] / 2, freq['o' - 'a'] / 2),
                        freq['n' - 'a']
                    )    
                );
    }
}
