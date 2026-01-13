# 648. Replace Words
# in python
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()

        for i in range(len(words)):
            word = words[i]
            prefix = ""
            for ch in word:
                prefix += ch
                if prefix in roots:
                    words[i] = prefix
                    break

        return " ".join(words)

# in java
class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        Set<String> set = new HashSet<>(dictionary);
        String[] words = sentence.split(" ");

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            String prefix = "";

            for (char c : word.toCharArray()) {
                prefix += c;
                if (set.contains(prefix)) {
                    words[i] = prefix;
                    break;
                }
            }
        }
        return String.join(" ", words);
    }
}
