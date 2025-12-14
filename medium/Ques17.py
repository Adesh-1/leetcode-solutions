# 17. Letter Combinations of a Phone Number
# in python
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = [""]

        for d in digits:
            new = []
            for s in res:
                for ch in phone[d]:
                    new.append(s + ch)
            res = new

        return res

# in java
class Solution {
    List<String> res = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return res;

        String[] phone = {
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        backtrack(digits, 0, new StringBuilder(), phone);
        return res;
    }

    private void backtrack(String digits, int idx,
                           StringBuilder cur, String[] phone) {

        if (idx == digits.length()) {
            res.add(cur.toString());
            return;
        }

        String letters = phone[digits.charAt(idx) - '0'];

        for (char c : letters.toCharArray()) {
            cur.append(c);
            backtrack(digits, idx + 1, cur, phone);
            cur.deleteCharAt(cur.length() - 1); # // backtrack
        }
    }
}
