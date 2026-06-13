# 3838. Weighted Word Mapping
# in python
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []

        for word in words:
            mod = sum(weights[ord(ch) - ord("a")] for ch in word) % 26
            res.append(chr(ord("z") - mod))

        return "".join(res)

# in java
class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            int sum = 0;
            for (char ch : word.toCharArray())
                sum += weights[ch - 'a'];
            int mod = sum % 26;
            sb.append((char) ('z' - mod));
        }
        return sb.toString();
    }
}
