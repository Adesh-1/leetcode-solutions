# 1925. Count Square Sum Triples
# in python
class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                s = a * a + b * b
                c_val = int(sqrt(s))
                if c_val <= n and c_val * c_val == s:
                    c += 1
        return c

# in java
class Solution {
    public int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int s = a * a + b * b;
                int c = (int) Math.sqrt(s);
                if (c <= n && c * c == s)
                    count++;
            }
        }
        return count;
    }
}
