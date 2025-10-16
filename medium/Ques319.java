// 319. Bulb Switcher
// in java
class Solution {
    public int bulbSwitch(int n) {
        // in simple count the perfect squares less than or equals to n
        int c = 0;
        for (int i = 1; i * i <= n; i++)
            c++;
        return c;
    }
}

// in python
import math as m
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(m.sqrt(n))
