# 2000. Reverse Prefix of Word
# in py
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)  # find first occurrence
        if idx == -1:
            return word  # if not found, return unchanged
        prefix = word[: idx + 1]  # slice up to and including idx
        return prefix[::-1] + word[idx + 1 :]

# in java
class Solution {
    public String reversePrefix(String word, char ch) {
        int ind = word.indexOf(ch);
        String s = "";
        if (ind == -1)
            return word;
        for(int i = ind; i >= 0;i--)
            s+=word.charAt(i);
        for(int i = ind + 1; i < word.length(); i++)
            s+=word.charAt(i);
        return s;
    } 
}
