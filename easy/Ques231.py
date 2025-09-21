# 231. Power of Two
# in python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))

# in java
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}

# more more info follow below link
# https://chatgpt.com/share/68d03c2a-c5bc-8001-b7db-584feb3d2665
