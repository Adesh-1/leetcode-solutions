// 7. Reverse Integer
// in python 
class Solution:
    def reverse(self, x: int) -> int:
        x1 = str(abs(x))
        x2 = x1[::-1]
        res = int(x2)
        if x < 0:
            res = -res 
        if res > 2**31 - 1 or res < -(2**31):
            res = 0
        return res

// in java
class Solution {
    public int reverse(int x) { 
        long res = 0;
        int n = x;
        if (n < 0){
            n = -n; // if n=-2 then it becomes -(-2) --> 2 (+ive)
        }
        while(n > 0){
            int r = n%10;
            res = r + (res*10);
            n /= 10;
        }
        if (x < 0){
            res = -res;
        }
        if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE){
            res = 0;
        }
        return (int) res;
    }
}
