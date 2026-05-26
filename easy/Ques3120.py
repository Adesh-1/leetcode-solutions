# 3120. Count the Number of Special Characters I
# in python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch.lower())

        return len(lower & upper)

# in java
class Solution {
    public int numberOfSpecialChars(String word) {
        Set<Character> lower = new HashSet<>();
        Set<Character> upper = new HashSet<>();
        for (char ch : word.toCharArray()) {
            if (Character.isLowerCase(ch))
                lower.add(ch);
            else
                upper.add(Character.toLowerCase(ch));
        }

        int count = 0;
        for (char ch : lower) {
            if (upper.contains(ch))
                count++;
        }

        return count;
    }
}
