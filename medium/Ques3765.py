# 3765. Complete Prime Number
# in python
class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def completePrime(self, num: int) -> bool:
        s = str(num)

        # check prefixes
        for i in range(1, len(s) + 1):
            if not self.isPrime(int(s[:i])):
                return False

        # check suffixes
        for i in range(len(s)):
            if not self.isPrime(int(s[i:])):
                return False

        return True

# in java
    # same logic as like python
class Solution {

    private boolean isPrime(int n) {
        if (n < 2) return false;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    public boolean completePrime(int num) {
        String s = String.valueOf(num);

        # // check prefixes
        for (int i = 1; i <= s.length(); i++) {
            int prefix = Integer.parseInt(s.substring(0, i));
            if (!isPrime(prefix)) return false;
        }

        # // check suffixes
        for (int i = 0; i < s.length(); i++) {
            int suffix = Integer.parseInt(s.substring(i));
            if (!isPrime(suffix)) return false;
        }

        return true;
    }
}
