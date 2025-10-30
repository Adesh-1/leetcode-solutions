# 3099. Harshad Number
# in python
class Solution:
    def sumOfDigit(self, n):
        sum = 0
        while n != 0:
            rem = n % 10
            sum += rem
            n //= 10
        return sum

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = self.sumOfDigit(x)
        if x % s == 0:
            return s
        else:
            return -1

# in java
class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int n = x;
        while (n != 0) {
            int r = n % 10;
            sum += r;
            n /= 10;
        }
        if (x % sum == 0)
            return sum;
        else
            return -1;
    }
}
