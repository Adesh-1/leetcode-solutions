# 3871. Count Commas in Range II
# in python
class Solution:
    def countCommas(self, n: int) -> int:
        ans, power = 0, 1000

        while power <= n:
            ans += n - power + 1
            power *= 1000

        return ans

# in java
class Solution {
    public long countCommas(long n) {
        long ans = 0;
        long power = 1000;

        while (power <= n) {
            ans += n - power + 1;
            power *= 1000;
        }

        return ans;
    }
}
