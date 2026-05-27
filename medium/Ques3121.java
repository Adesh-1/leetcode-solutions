// 3121. Count the Number of Special Characters II
// in java
class Solution {
    public int numberOfSpecialChars(String word) {

        int[] lower = new int[26];
        int[] upper = new int[26];

        // initialize
        for (int i = 0; i < 26; i++) {
            lower[i] = -1;
            upper[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < word.length(); i++) {

            char ch = word.charAt(i);

            if (Character.isLowerCase(ch)) {

                lower[ch - 'a'] = i; // last lowercase index

            } else {

                if (upper[ch - 'A'] == Integer.MAX_VALUE) {
                    upper[ch - 'A'] = i; // first uppercase index
                }
            }
        }

        int count = 0;

        for (int i = 0; i < 26; i++) {

            if (lower[i] != -1 &&
                upper[i] != Integer.MAX_VALUE &&
                lower[i] < upper[i]) {

                count++;
            }
        }

        return count;
    }
}


// in python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i, ch in enumerate(word):

            if ch.islower():
                lower[ch] = i          // # last lowercase position

            else:
                if ch not in upper:
                    upper[ch] = i      // # first uppercase position

        count = 0

        for ch in lower:
            if ch.upper() in upper:
                if lower[ch] < upper[ch.upper()]:
                    count += 1

        return count
