# 357. Count Numbers with Unique Digits
# in python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        n = min(n, 10)  # more than 10 digits isn't possible with unique digits
        count = 10      # all numbers with 1 digit
        unique = 9      # choices for first digit (1-9)
        available = 9   # remaining digits for subsequent positions

        for length in range(2, n + 1):
            unique *= available
            count += unique
            available -= 1
        
        return count

# in java
class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        if (n == 1) return 10;

        n = Math.min(n, 10);  # // more than 10 digits isn't possible with unique digits
        int count = 10;       # // all 1-digit numbers
        int unique = 9;       # // choices for first digit in numbers >= 2 digits
        int available = 9;    # // remaining digits for subsequent positions

        for (int length = 2; length <= n; length++) {
            unique *= available;
            count += unique;
            available--;
        }

        return count;
    }
}
