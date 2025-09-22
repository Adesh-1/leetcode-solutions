// 326. Power of Three
// in java
class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0)
            return false;
        while (n % 3 == 0)
            n /= 3;
        return n == 1;
    }
}

// in python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        l = set([pow(3, i) for i in range(20)])  // # using trick 😂😂
        return n in l
