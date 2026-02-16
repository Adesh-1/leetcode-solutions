# 190. Reverse Bits
# in python
  # 1st method
class Solution:
    def reverseBits(self, n: int) -> int:
        b = f"{n:032b}"  # always 32-bit binary
        return int(b[::-1], 2)

    # 2nd method (Best Interview Approach (Bit Manipulation))
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

    # 3rd mehtod
class Solution:
    def reverseBits(self, n: int) -> int:
        b = f"{n:b}"
        bl = list(b)
        bl.reverse()
        # add 0 in last until len of binary list != 32
        while len(bl) != 32:
            bl.append("0")
        return int("".join(bl), 2)  # join the list then convert into binary

# in java
  # 1st method (Best Interview Approach (Bit Manipulation))
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

    # 2nd method
class Solution {
    public int reverseBits(int n) {
        String s = Integer.toBinaryString(n);
        String s1 = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            s1 += s.charAt(i);
        }
        while (s1.length() < 32)
            s1 += "0";
        int a = Integer.parseInt(s1, 2);
        return a;
    }
}
