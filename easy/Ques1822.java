// 1822. Sign of the Product of an Array
// in java
class Solution {
    static int signFunc(int x) {
        if (x > 0)
            return 1;
        else if (x < 0)
            return -1;
        else
            return 0;
    }
    public int arraySign(int[] nums) {
        int sign = 1;
        for (int i : nums) {
            if (i == 0)
                return 0;
            else if (i < 0)
                sign = -sign;
        }
        return signFunc(sign);
    }
}

// in python
class Solution:
    def signFunc(self, sign):
        if sign > 0:
            return 1
        elif sign < 0:
            return -1
        else:
            return 0

    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                sign = -sign
        return self.signFunc(sign)
