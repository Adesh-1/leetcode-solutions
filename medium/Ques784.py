# 784. Letter Case Permutation
# in python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(i, path):
            if i == len(s):
                res.append(path)
                return

            if s[i].isalpha():
                backtrack(i + 1, path + s[i].lower())
                backtrack(i + 1, path + s[i].upper())
            else:
                backtrack(i + 1, path + s[i])

        backtrack(0, "")
        return res

# in java
class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<>();
        res.add("");

        for (char ch : s.toCharArray()) {
            List<String> newRes = new ArrayList<>();

            if (Character.isLetter(ch)) {
                for (String str : res) {
                    newRes.add(str + Character.toLowerCase(ch));
                    newRes.add(str + Character.toUpperCase(ch));
                }
            } else {
                for (String str : res) {
                    newRes.add(str + ch);
                }
            }

            res = newRes;
        }

        return res;
    }
}
