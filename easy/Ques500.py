# 500. Keyboard Row
# in python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        for w in words:
            lower = set(w.lower())
            if lower <= row1 or lower <= row2 or lower <= row3:
                # In Python, A <= B means A is a subset of B i.e. Every element of A is also in B.
                ans.append(w)
        return ans

# in java
class Solution {
    private boolean inOneRow(String word, String row) {
        for (char c : word.toCharArray()) {
            if (row.indexOf(c) == -1)
                return false;
        }
        return true;
    }

    public String[] findWords(String[] words) {
        String row1 = "qwertyuiop";
        String row2 = "asdfghjkl";
        String row3 = "zxcvbnm";

        List<String> ans = new ArrayList<>();

        for (String w : words) {
            String lower = w.toLowerCase();
            if (inOneRow(lower, row1) || inOneRow(lower, row2) || inOneRow(lower, row3)) {
                ans.add(w);
            }
        }

        return ans.toArray(new String[0]);
    }
}
