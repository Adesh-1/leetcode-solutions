# 3536. Maximum Product of Two Digits
# in python
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(map(int, str(n)), reverse=True)
        return digits[0] * digits[1]

# in java
class Solution {
    public int maxProduct(int n) {
        int first = 0, second = 0;
        while (n != 0) {
            int digit = n % 10;
            if (digit >= first) {
                second = first;
                first = digit;
            } else if (digit > second)
                second = digit;
            n /= 10;
        }
        return first * second;
    }
}
