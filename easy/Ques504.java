// 504. Base 7
// in java
class Solution {
    public String convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }

        String sign = num < 0 ? "-" : "";
        num = Math.abs(num);

        StringBuilder ans = new StringBuilder();

        while (num > 0) {
            ans.insert(0, num % 7); // add digit at front (i.e. add at index 0)
            num /= 7;
        }

        return sign + ans.toString();
    }
}

// in python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        sign = "-" if num < 0 else ""
        num = abs(num)

        ans = ""
        while num:
            ans = str(num % 7) + ans
            num //= 7

        return sign + ans
