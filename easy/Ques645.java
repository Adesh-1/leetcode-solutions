// 645. Set Mismatch
// in java
class Solution {
    public int[] findErrorNums(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int dup = -1;

        // Find duplicate number
        for (int x : nums) {
            if (set.contains(x)) {
                dup = x;
            }
            set.add(x);
        }

        // Find missing number
        int n = nums.length;
        int totalExpected = n * (n + 1) / 2;

        int sumSet = 0;
        for (int x : set) {
            sumSet += x;
        }

        int missing = totalExpected - sumSet;

        return new int[] {dup, missing};
    }
}

// in python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s, dup = set(), -1
        for i in nums:
            if i in s:
                dup = i
            s.add(i)
        missing = sum(range(1, len(nums) + 1)) - sum(s)
        return [dup, missing]
