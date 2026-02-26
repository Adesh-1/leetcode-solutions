# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# in python
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        n = int(s, 2)
        while n != 1:
            n = n // 2 if n % 2 == 0 else n + 1   # ternary operator
            steps += 1
        return steps

# in java
class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;

        # // Traverse from right to left (ignore first bit)
        for (int i = s.length() - 1; i > 0; i--) {
            int bit = s.charAt(i) - '0';

            if (bit + carry == 1) {
                steps += 2;   # // +1 operation and divide by 2
                carry = 1;    # // carry generated
            } else {
                steps += 1;   # // only divide by 2
            }
        }

        return steps + carry;
    }
}
