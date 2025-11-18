 // 461. Hamming Distance
// in java
class Solution {
    public int hammingDistance(int x, int y) {
        int n = x ^ y;  // XOR to find differing bits
        int count = 0;

        while (n > 0) {
            count += n & 1;  // check last bit
            n >>= 1;         // shift right
        }

        return count;
    }
}

// in python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
