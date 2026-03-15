# 720. Longest Word in Dictionary
# in python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        valid = set()
        ans = ""

        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans

# in java
class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words);
        Set<String> set = new HashSet<>();
        String ans = "";

        for (String word : words) {
            if (word.length() == 1 || set.contains(word.substring(0, word.length() - 1))) {
                set.add(word);
                if (word.length() > ans.length()) {
                    ans = word;
                }
            }
        }
        return ans;
    }
}
