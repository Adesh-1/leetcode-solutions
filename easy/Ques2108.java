// 2108. Find First Palindromic String in the Array
// in java
class Solution {
    public String firstPalindrome(String[] words) {
        for (String word : words) {
            String revWord = new StringBuilder(word).reverse().toString();
            if (word.equals(revWord))
                return word;
        }
        return "";
    }
}

// in python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
  
