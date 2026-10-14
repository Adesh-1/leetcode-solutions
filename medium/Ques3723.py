# 3723. Maximize Sum of Squares of Digits
# in python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines, rem = divmod(sum, 9)
        return "9" * nines + (str(rem) if rem else "") + "0" * (num - nines - bool(rem))


# in java
class Solution {
    public String maxSumOfSquares(int num, int sum) {
        if (sum > 9 * num)
            return "";
        StringBuilder ans = new StringBuilder();
        while (sum >= 9) {
            ans.append('9');
            sum -= 9;
        }
        if (sum > 0)
            ans.append((char) ('0' + sum));
        while (ans.length() < num)
            ans.append('0');
        return ans.toString();
    }
}
