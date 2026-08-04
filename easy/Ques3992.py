# 3992. Rearrange String to Avoid Character Pair
# in python
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xs, others, ys = [], [], []

        for ch in s:
            if ch == y:
                ys.append(ch)
            elif ch == x:
                xs.append(ch)
            else:
                others.append(ch)

        return "".join(ys + others + xs)

# in java
class Solution {
    public String rearrangeString(String s, char x, char y) {
        StringBuilder ys = new StringBuilder();
        StringBuilder others = new StringBuilder();
        StringBuilder xs = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (ch == y)
                ys.append(ch);
            else if (ch == x)
                xs.append(ch);
            else
                others.append(ch);
        }
        return ys.toString() + others.toString() + xs.toString();
    }
}
