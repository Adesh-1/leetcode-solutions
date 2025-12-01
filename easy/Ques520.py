# 520. Detect Capital
# in python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1 or 2
        if word.isupper() or word.islower():
            return True
        # Case 3: first uppercase, rest lowercase (works for length 1 too)
        return word[0].isupper() and word[1:].islower()

# in java
class Solution {
    public boolean detectCapitalUse(String word) {
        # // Case 1 or 2: all uppercase or all lowercase
        if (word.equals(word.toUpperCase()) || word.equals(word.toLowerCase()))
            return true;

        # // Case 3: first uppercase, rest lowercase
        return Character.isUpperCase(word.charAt(0)) &&
               word.substring(1).equals(word.substring(1).toLowerCase());
    }
}
