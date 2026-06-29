# 1967. Number of Strings That Appear as Substrings in Word
# in python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c = 0
        for i in patterns:
            if i in word:
                c += 1
        return c

# in java
class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count = 0;
        for (String s : patterns)
            if (word.contains(s))
                count++;
        return count;
    }
}
