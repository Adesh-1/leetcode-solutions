# 77. Combinations
# in python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return

            for num in range(start, n + 1):
                curr.append(num)
                backtrack(num + 1, curr)
                curr.pop()

        backtrack(1, [])
        return res

# in java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int start, int n, int k,
                           List<Integer> curr,
                           List<List<Integer>> res) {

        # // base case
        if (curr.size() == k) {
            res.add(new ArrayList<>(curr));
            return;
        }

        # // try all numbers from start to n
        for (int i = start; i <= n; i++) {
            curr.add(i);                          # // choose
            backtrack(i + 1, n, k, curr, res);   # // explore
            curr.remove(curr.size() - 1);        # // un-choose (backtrack)
        }
    }
}
