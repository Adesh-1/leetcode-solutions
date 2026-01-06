# 537. Complex Number Multiplication
# in python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # split both numbers into real and imaginary parts
        a, b = num1.split("+")
        c, d = num2.split("+")

        # convert to integers (remove 'i' from imaginary part)
        a = int(a)
        b = int(b[:-1])
        c = int(c)
        d = int(d[:-1])

        # apply formula: (a+bi)(c+di)
        real = a * c - b * d
        imag = a * d + b * c

        # return in required format
        return f"{real}+{imag}i"

# in java
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        # // split both strings
        String[] p1 = num1.split("\\+");
        String[] p2 = num2.split("\\+");

        # // real and imaginary parts
        int a = Integer.parseInt(p1[0]);
        int b = Integer.parseInt(p1[1].replace("i", ""));
        int c = Integer.parseInt(p2[0]);
        int d = Integer.parseInt(p2[1].replace("i", ""));

        # // (a+bi)(c+di)
        int real = a * c - b * d;
        int imag = a * d + b * c;

        return real + "+" + imag + "i";
    }
}
