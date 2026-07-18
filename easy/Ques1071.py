# 1071. Greatest Common Divisor of Strings
# in python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        return str1[: gcd(len(str1), len(str2))]

# in java
class Solution {
    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1))
            return "";
        return str1.substring(0, gcd(str1.length(), str2.length()));
    }
}
