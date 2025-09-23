// 2119. A Number After a Double Reversal
// in java
class Solution {
    public boolean isSameAfterReversals(int num) {
        // If num == 0, always true
        if (num == 0) return true;

        // If num ends with 0, after double reversal it changes
        return num % 10 != 0;
    }
}

// in pyhton
class Solution:
    def reverse(self, n: int) -> int:
        rev = 0
        while n != 0:
            rem = n % 10
            rev = rev * 10 + rem
            n //= 10
        return rev

    def isSameAfterReversals(self, num: int) -> bool:
        first_rev = self.reverse(num)
        second_rev = self.reverse(first_rev)
        return second_rev == num


// for more information of pyhton properties follow below link
// https://chatgpt.com/share/68d2d54e-32b0-8001-8f28-25ab4ed78fdb
