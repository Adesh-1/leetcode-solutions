# 633. Sum of Square Numbers
# in python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)

        while left <= right:
            s = left * left + right * right
            if s == c:
                return True
            elif s < c:
                left += 1
            else:
                right -= 1

        return False

# in java
class Solution {
    public boolean judgeSquareSum(int c) {
        long left = 0;
        long right = (long) Math.sqrt(c);
        while (left <= right) {
            long sum = left * left + right * right;
            if (sum == c)
                return true;
            else if (sum < c)
                left++;
            else
                right--;
        }
        return false;
    }
}
