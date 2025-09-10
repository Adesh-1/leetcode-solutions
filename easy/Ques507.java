// 507. Perfect Number
// in java
class Solution {
    private static final int[] PERFECT_NUMBERS = {
            6, 28, 496, 8128, 33550336
    };

    public boolean checkPerfectNumber(int num) {
        for (int perfect : PERFECT_NUMBERS) {
            if (num == perfect)
                return true;
        }
        return false;
    }
}

// in python
class Solution:
    PERFECT_NUMBERS = [6, 28, 496, 8128, 33550336]

    def checkPerfectNumber(self, num: int) -> bool:
        return num in self.PERFECT_NUMBERS
