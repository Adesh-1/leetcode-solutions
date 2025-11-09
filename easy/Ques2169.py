# 2169. Count Operations to Obtain Zero
# in python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op = 0
        while num1 and num2:
            if num1 >= num2:
                op += num1 // num2
                num1 = num1 % num2
            else:
                op += num2 // num1
                num2 = num2 % num1
        return op

# in java
class Solution {
    public int countOperations(int num1, int num2) {
        int op = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 < num2) {
                num2 -= num1;
            } else { #// num1 >= num2
                num1 -= num2;
            }
            op++;
        }
        return op;
    }
}
