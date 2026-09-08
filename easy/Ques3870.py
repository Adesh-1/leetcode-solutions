# 3870. Count Commas in Range
# in python
class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)

# in java
class Solution {
    public int countCommas(int n) {
        return Math.max(n - 999, 0);
    }
}
