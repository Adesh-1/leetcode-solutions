# 29. Divide Two Integers
# in python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)
        return min(max(res, -(2**31)), 2**31 - 1)

  # in java
  class Solution {
    public int divide(int dividend, int divisor) {
        long dividendL = (long) dividend;
        long divisorL = (long) divisor;
        long res = dividendL / divisorL;
        if (res > Integer.MAX_VALUE)
            return Integer.MAX_VALUE;
        if (res < Integer.MIN_VALUE)
            return Integer.MIN_VALUE;

        return (int) res;
    }
}
