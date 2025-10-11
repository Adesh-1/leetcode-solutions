# 167. Two Sum II - Input Array Is Sorted
# in python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1

# in java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int l = 0;
        int r = n - 1;
        while (l < r) {
            int total = numbers[l] + numbers[r];
            if (total == target)
                return new int[] { l + 1, r + 1 };
            else if (total < target)
                l++;
            else
                r--;
        }
        return new int[] {};
    }
}
