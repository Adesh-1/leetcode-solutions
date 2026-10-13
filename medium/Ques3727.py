# 3727. Maximum Alternating Sum of Squares
# in python
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)

        half = len(nums) // 2

        ans = sum(num**2 for num in nums[half:])  # 2nd half be positive
        ans -= sum(num**2 for num in nums[:half])  # 1st half be negative

        return ans

# in java
class Solution {
    public long maxAlternatingSum(int[] nums) {
        int[] arr = Arrays.stream(nums)
                          .map(Math::abs)
                          .sorted()
                          .toArray();

        int half = arr.length / 2;
        long ans = 0;

        for (int i = half; i < arr.length; i++) {
            ans += (long) arr[i] * arr[i];
        }

        for (int i = 0; i < half; i++) {
            ans -= (long) arr[i] * arr[i];
        }

        return ans;
    }
}
