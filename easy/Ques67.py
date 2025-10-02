# 67. Add Binary
# in python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = int(a, 2) + int(b, 2)
        return bin(total)[2:]

# in java
import java.math.BigInteger;

class Solution {
    public String addBinary(String a, String b) {
        BigInteger num1 = new BigInteger(a, 2);
        BigInteger num2 = new BigInteger(b, 2);
        
        BigInteger sum = num1.add(num2);
        
        return sum.toString(2);
    }
}
