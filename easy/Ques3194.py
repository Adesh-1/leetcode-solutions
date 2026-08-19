# 3194. Minimum Average of Smallest and Largest Elements
# in python
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        return min((nums[i] + nums[n - i - 1]) / 2 for i in range(n // 2))

# in java
class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        int j = nums.length - 1;
        double minAvg = Double.MAX_VALUE;

        for (int i = 0; i < nums.length; i++) {
            double avg = (nums[i] + nums[j]) / 2.0;
            minAvg = Math.min(minAvg, avg);
            j--;
        }

        return minAvg;
    }
}
