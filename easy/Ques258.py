# 258. Add Digits
# in python
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(list(map(int, list(str(num)))))
        return num

  # in java
  class Solution {
    public int addDigits(int num) {
        int n = num;
        while (n > 9) {
            int sum = 0;
            while (n != 0) {
                int rem = n % 10;
                sum += rem;
                n /= 10;
            }
            n = sum;
        }
        return n;
    }
}
