# 670. Maximum Swap
# in python
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        
        # Store last occurrence of each digit
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i in range(len(digits)):
            for d in range(9, int(digits[i]), -1):
                if d in last and last[d] > i:
                    # Swap
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int("".join(digits))
        
        return num

# in java
class Solution {
    public int maximumSwap(int num) {
        char[] digits = Integer.toString(num).toCharArray();
        
        int[] last = new int[10];
        
        # // Store last occurrence of each digit
        for (int i = 0; i < digits.length; i++) {
            last[digits[i] - '0'] = i;
        }
        
        for (int i = 0; i < digits.length; i++) {
            for (int d = 9; d > digits[i] - '0'; d--) {
                if (last[d] > i) {
                    # // Swap
                    char temp = digits[i];
                    digits[i] = digits[last[d]];
                    digits[last[d]] = temp;
                    
                    return Integer.parseInt(new String(digits));
                }
            }
        }
        
        return num;
    }
}
