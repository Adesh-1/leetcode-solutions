# 3379. Transformed Array
# in python
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                new_index = (i + nums[i]) % n 
                result[i] = nums[new_index]

        return result

        # a % b = a - b * floor(a / b) in python modulo works like this
# for more info follow below link -->
    # https://chatgpt.com/share/6984d9c8-0090-800c-a6cb-b82a4d8a044c

# in java
class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                result[i] = 0;
            } else {
                int newIndex = ((i + nums[i]) % n + n) % n;
                result[i] = nums[newIndex];
            }
        }

        return result;
    }
}
