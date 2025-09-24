# 1342. Number of Steps to Reduce a Number to Zero
# in python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            # conditional expression or ternary operator
            num = num // 2 if num % 2 == 0 else num - 1
            step += 1
        return step

# in java
  class Solution {
    public int numberOfSteps(int num) {
        int step = 0;
        while (num != 0) {
            # // ternary operator
            num = (num % 2 == 0) ? num / 2 : num - 1;
            step++;
        }
        return step;
    }
}
