# 338. Counting Bits
# in python
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # i >> 1 is i//2, i & 1 is i%2
        return ans

# in java
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1); // i>>1 is i/2, i&1 is i%2
        }
        return ans;
    }
}
