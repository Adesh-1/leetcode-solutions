// 70. Climbing Stairs
// in java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2)
            return n;
        int a = 1, b = 2;
        for (int i = 3; i < n + 1; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}

// in python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

  
