# 2828. Check if a String Is an Acronym of Words
# in python
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        for i in range(len(words)):
            if len(words[i]) == 0 or words[i][0] != s[i]:
                return False

        return True

# in java
class Solution {
    public boolean isAcronym(List<String> words, String s) {
        if (words.size() != s.length())
            return false;

        for (int i = 0; i < words.size(); i++) {
            if (words.get(i).length() == 0 || words.get(i).charAt(0) != s.charAt(i))
                return false;
        }
        return true;
    }
}
