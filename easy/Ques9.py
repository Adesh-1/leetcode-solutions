# 9. Palindrome Number
# in python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        i = int(s[::-1])
        return x == i

  # in java
  class Solution {
    public boolean isPalindrome(int x) {
        boolean res = false;
        int rev = 0;
        int n = x;
        if (n < 0 || (n % 10 == 0 && n != 0)) {
            return res;
        }
        while (n > 0) {
            int r = n % 10;
            rev = r + (rev * 10);
            n /= 10;
        }
        if (x == rev)
            res = true;
        return res;
    }
}
