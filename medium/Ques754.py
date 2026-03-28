# 754. Reach a Number
# in python
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)  # make positive
        total = 0
        k = 0        
        while total < target or (total - target) % 2 != 0:
            k += 1
            total += k
        return k

# in java
class Solution {
    public int reachNumber(int target) {
        target = Math.abs(target);  
        
        int sum = 0;
        int k = 0;
        
        while (sum < target || (sum - target) % 2 != 0) {
            k++;
            sum += k;
        }
        
        return k;
    }
}
