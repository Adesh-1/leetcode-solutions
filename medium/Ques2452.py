# 2452. Words Within Two Edits of Dictionary
# in python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def within_2_edits(q, d):
            diff = 0
            for i in range(len(q)):
                if q[i] != d[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        res = []
        for q in queries:
            for d in dictionary:

                if within_2_edits(q, d):
                    res.append(q)
                    break  # found a match, move to next query
        return res

# in java
class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        List<String> ans = new ArrayList<>();

        for (String q : queries) {
            for (String d : dictionary) {
                if (withinTwoEdits(q, d)) {
                    ans.add(q);
                    break;
                }
            }
        }

        return ans;
    }

    private boolean withinTwoEdits(String a, String b) {
        int diff = 0;

        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i) && ++diff > 2) {
                return false;
            }
        }

        return true;
    }
}
