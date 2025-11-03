// 371. Sum of Two Integers
// in java
class Solution {
    public int getSum(int a, int b) {
        return a + b;
    }
}

// in python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits mask in hexadecimal
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        
        return a if a <= MAX_INT else ~(a ^ MASK)
