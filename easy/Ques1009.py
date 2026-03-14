# 1009. Complement of Base 10 Integer
# in python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = f"{n:b}"
        b = "".join("1" if c == "0" else "0" for c in b)
        return int(b, 2)

# in java
class Solution {
    public int bitwiseComplement(int n) {
        String b = Integer.toBinaryString(n);
        b = b.replace('0', 'x').replace('1', '0').replace('x', '1');
        return Integer.parseInt(b, 2);
    }
}
