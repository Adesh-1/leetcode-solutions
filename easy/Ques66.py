# 66. Plus One
# in python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits))) + 1
        return list(map(int, str(n)))

# in java
import java.math.BigInteger;

class Solution {
    public int[] plusOne(int[] digits) {

        StringBuilder sb = new StringBuilder();
        for (int d : digits) {
            sb.append(d);
        }

        BigInteger n = new BigInteger(sb.toString());
        n = n.add(BigInteger.ONE);

        String numStr = n.toString();
        int[] result = new int[numStr.length()];

        for (int i = 0; i < numStr.length(); i++) {
            result[i] = numStr.charAt(i) - '0';
        }

        return result;
    }
}
