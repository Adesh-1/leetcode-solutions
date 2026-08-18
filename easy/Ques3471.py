# 3471. Find the Largest Almost Missing Integer
# in python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = [0] * 51
      
        for i in range(len(nums) - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            for s in seen:
                count[s] += 1

        ans = -1
        for i in range(51):
            if count[i] == 1:
                ans = i

        return ans

# in java
class Solution {
    public int largestInteger(int[] nums, int k) {
        int[] count = new int[51];
        Set<Integer> seen = new HashSet<>();

        for (int i = 0; i <= nums.length - k; i++) {
            seen.clear();

            for (int j = i; j < i + k; j++)
                seen.add(nums[j]);

            for (int s : seen)
                count[s]++;
        }

        int ans = -1;

        for (int i = 0; i < 51; i++)
            if (count[i] == 1)
                ans = i;

        return ans;
    }
}
