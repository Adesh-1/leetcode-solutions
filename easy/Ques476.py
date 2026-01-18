# 476. Number Complement
# in python
class Solution:
    def findComplement(self, num: int) -> int:
        b = f"{num:b}"
        c = "".join("1" if i == "0" else "0" for i in b)
        return int(c, 2)

# in java
class Solution {
    public int findComplement(int num) {
        String bin = Integer.toBinaryString(num);
        StringBuilder sb = new StringBuilder();

        for (char c : bin.toCharArray()) {
            sb.append(c == '0' ? '1' : '0');
        }

        return Integer.parseInt(sb.toString(), 2);
    }
}
