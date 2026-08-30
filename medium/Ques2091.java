// 2091. Removing Minimum and Maximum From Array
// in python
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))

        left = max(mini, maxi) + 1
        right = n - min(mini, maxi)
        both = min(mini, maxi) + 1 + n - max(mini, maxi)

        return min(left, right, both)

// in java
  class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;

        int minInd = 0;
        int maxInd = 0;

        for (int i = 1; i < n; i++) {
            // minimum element
            if (nums[i] < nums[minInd])
                minInd = i;

            // maximum element
            if (nums[i] > nums[maxInd])
                maxInd = i;
        }

        int left = Math.max(minInd, maxInd) + 1;
        int right = n - Math.min(minInd, maxInd);
        int both = Math.min(minInd, maxInd) + 1 + n - Math.max(minInd, maxInd);

        return Math.min(both, Math.min(left, right));
    }
}
