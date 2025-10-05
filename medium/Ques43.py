# 43. Multiply Strings
# in python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

  # in java
  import java.math.BigInteger;

class Solution {
    public String multiply(String num1, String num2) {
        BigInteger n1 = new BigInteger(num1);
        BigInteger n2 = new BigInteger(num2);
        BigInteger res = n1.multiply(n2);
        return res.toString();
    }
}
