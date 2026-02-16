# 190. Reverse Bits
# in python
  # 1st method
class Solution:
    def reverseBits(self, n: int) -> int:
        b = f"{n:032b}"  # always 32-bit binary
        return int(b[::-1], 2)

# in java
  # 1st method
public class Solution {
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        return result;
    }
}
