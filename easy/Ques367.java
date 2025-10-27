// 367. Valid Perfect Square
// in java
class Solution {
    public boolean isPerfectSquare(int num) {
        int sq = (int) Math.sqrt(num);
        return sq * sq == num;
    }
}

// in python
import math as m
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq = m.sqrt(num)
        return sq.is_integer()
