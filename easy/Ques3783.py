# 3783. Mirror Distance of an Integer
# in python
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))

# in java
class Solution {
    public int mirrorDistance(int n) {
        int x = n;
        int rev = 0;
        while (x != 0) {
            int r = x % 10;
            rev = rev * 10 + r;
            x /= 10;
        }
        return Math.abs(n - rev);
    }
}
