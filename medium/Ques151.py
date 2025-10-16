# 151. Reverse Words in a String
# in python
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split()
        l.reverse()
        return " ".join(l)

# in java
class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder res = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            res.append(words[i]);
            if (i != 0)
                res.append(" ");
        }
        return res.toString();
    }
}
