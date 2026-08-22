# 3622. Check Divisibility by Digit Sum and Product
# in python
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit = list(map(int, str(n)))
        return n % (sum(digit) + prod(digit)) == 0

# in java
class Solution {
    public boolean checkDivisibility(int n) {
        int sum = 0;
        int mul = 1;

        int temp = n;
        while (temp > 0) {   # // can be "temp != 0"
            int rem = temp % 10;
            sum += rem;
            mul *= rem;
            temp /= 10;
        }

        return n % (sum + mul) == 0;
    }
}
