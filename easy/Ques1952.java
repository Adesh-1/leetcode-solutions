// 1952. Three Divisors
// in java
class Solution {
    public boolean isThree(int n) {
        int c = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0)
                c++;
        }
        return c == 3;
    }
}

// in python
class Solution:
    def isThree(self, n: int) -> bool:
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
        return c == 3 
