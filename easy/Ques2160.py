# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# in python
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        num1 = int(digits[0] + digits[2])
        num2 = int(digits[1] + digits[3])
        return num1 + num2

# in java
class Solution {
    public int minimumSum(int num) {
        char[] arr = String.valueOf(num).toCharArray();
        Arrays.sort(arr);
        int num1 = (arr[0] - '0') * 10 + (arr[2] - '0');
        int num2 = (arr[1] - '0') * 10 + (arr[3] - '0');
        return num1 + num2;
    }
}
