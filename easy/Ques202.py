# 202. Happy Number
# in python
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = sum(pow(int(i), 2) for i in str(n))
        return n == 1

# in java
class Solution {
    public boolean isHappy(int n) {
        if (n == 1 || n == 7)
            return true;
        else if (n < 10)
            return false;
        else {
            int sum = 0;
            while (n > 0) {
                int temp = n % 10;
                sum += temp * temp;
                n = n / 10;
            }
            return isHappy(sum);
        }
    }
}
