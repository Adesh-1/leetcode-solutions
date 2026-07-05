# 2815. Max Pair Sum in an Array
# in python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum = [-1] * 10
        ans = -1
        for num in nums:

            # find largest digit
            largest = 0
            temp = num
            while temp != 0:
                largest = max(largest, temp % 10)
                temp //= 10

            if max_sum[largest] != -1:
                ans = max(ans, num + max_sum[largest])
                
            max_sum[largest] = max(max_sum[largest], num)
        return ans

# in java
class Solution {
    public int maxSum(int[] nums) {
        int[] maxNum = new int[10];
        Arrays.fill(maxNum, -1);
        int ans = -1;

        for (int num : nums) {
            int largest = 0;
            int temp = num;
            while (temp != 0) {
                largest = Math.max(largest, temp % 10);
                temp /= 10;
            }
            if (maxNum[largest] != -1)
                ans = Math.max(ans, num + maxNum[largest]);
            maxNum[largest] = Math.max(maxNum[largest], num);
        }
        return ans;
    }
}
