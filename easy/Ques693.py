# 693. Binary Number with Alternating Bits
# in python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = list(f"{n:b}")
        for i in range(len(b) - 1):
            if b[i] == b[i + 1]:
                return False
        return True

# in java
class Solution {
    public boolean hasAlternatingBits(int n) {
        String b = Integer.toBinaryString(n);
        for (int i = 0; i < b.length() - 1; i++) {
            if (b.charAt(i) == b.charAt(i + 1))
                return false;
        }
        return true;
    }
}
