# 345. Reverse Vowels of a String
# in python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)        # convert to list
        L, R = 0, len(s)-1
        while L < R:
            # move L until vowel
            while L < R and s[L] not in vowels:
                L += 1
            # move R until vowel
            while L < R and s[R] not in vowels:
                R -= 1
            # now both are vowels → swap
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1
        return "".join(s)

# in java
class Solution {
    public String reverseVowels(String s) {
        # // convert to char array
        char[] arr = s.toCharArray();

        int L = 0, R = arr.length - 1;

        while (L < R) {
            while (L < R && !isVowel(arr[L])) {
                L++;
            }
            while (L < R && !isVowel(arr[R])) {
                R--;
            }

            # // swap vowels
            char temp = arr[L];
            arr[L] = arr[R];
            arr[R] = temp;

            L++;
            R--;
        }

        return new String(arr);
    }

    private boolean isVowel(char c) {
        return "aeiouAEIOU".indexOf(c) != -1;
    }
}
