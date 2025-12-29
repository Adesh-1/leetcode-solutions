# 1015. Smallest Integer Divisible by K
# in python
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        cur = 0
        for length in range(1, k + 1):
            cur = ((cur * 10) + 1) % k  # This gives the same result as new = old * 10 + 1
                            # so we use ( (remainder_of_11 * 10) + 1 ) % K
            if cur == 0:
                return length
        return -1

# in java
class Solution {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0)
            return -1;
        int cur = 0;
        for (int len = 1; len < k + 1; len++) {
            cur = ((cur * 10) + 1) % k;
                    # // This gives the same result as new = old * 10 + 1
                    # // so we use ( (remainder_of_11 * 10) + 1 ) % K
            if (cur == 0)
                return len;
        }
        return -1;
    }
}
