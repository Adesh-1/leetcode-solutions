# 2427. Number of Common Factors
# in java
class Solution {
    public int commonFactors(int a, int b) {
        int count = 0;
        for (int i = 1; i <= Math.min(a, b); i++) {
            if ((a % i == 0) && (b % i == 0))
                count++;
        }
        return count;
    }
}

# in pyhton
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        for i in range(1, gcd(a, b) + 1): 
            #It only returns a single number → the greatest common divisor. 
                    # i.e. 1,2,3,6 in this it returns 6 greatest factor
            if a % i == 0 and b % i == 0:
                c += 1
        return c
