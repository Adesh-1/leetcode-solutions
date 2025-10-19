# 263. Ugly Number
# in python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        return n == 1

# in java
class Solution {
    public boolean isUgly(int n) {
        if (n <= 0)
            return false;
        int[] primes = { 2, 3, 5 };
        for (int p : primes) {
            while (n % p == 0) {
                n /= p;
            }
        }
        return n == 1;
    }
}
