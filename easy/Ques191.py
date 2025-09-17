# 191. Number of 1 Bits
# in pyhton
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:]
        return s.count('1')

# in java
class Solution {
    public int hammingWeight(int n) {
        String s = Integer.toBinaryString(n);
        int c = 0;
        for (char i : s.toCharArray()) {
            if (i == '1')
                c++;
        }
        return c;
    }
}
