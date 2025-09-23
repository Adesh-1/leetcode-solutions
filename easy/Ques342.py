# 342. Power of Four
# in python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        s = set([pow(4, i) for i in range(20)])
        return n in s

  # in java
  class Solution {
    public boolean isPowerOfFour(int n) {
        if (n <= 0)
            return false;
        while (n % 4 == 0)
            n /= 4;
        return n == 1;
    }
}
