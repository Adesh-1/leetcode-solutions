# 917. Reverse Only Letters
# in python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)

# in java
class Solution {
    public String reverseOnlyLetters(String s) {
        char[] ch = s.toCharArray();
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (!Character.isLetter(ch[i]))
                i++;
            else if (!Character.isLetter(ch[j]))
                j--;
            else {
                char temp = ch[i];
                ch[i] = ch[j];
                ch[j] = temp;
                i++;
                j--;
            }
        }
        return new String(ch);
    }
}
