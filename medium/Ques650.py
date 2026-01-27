# 650. 2 Keys Keyboard
# in python
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans

# in java
class Solution {
    public int minSteps(int n) {
        if (n == 1)
            return 0;
        int ans = 0;
        int d = 2;
        while (n > 1) {
            while (n % d == 0) {
                ans += d;
                n /= d;
            }
            d += 1;
        }
        return ans;
    }
}
