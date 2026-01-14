# 503. Next Greater Element II
# in python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            idx = i % n

            while stack and nums[idx] > nums[stack[-1]]:
                prev = stack.pop()
                res[prev] = nums[idx]

            if i < n:
                stack.append(idx)

        return res

# in java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < 2 * n; i++) {
            int idx = i % n;

            while (!stack.isEmpty() && nums[idx] > nums[stack.peek()]) {
                int prev = stack.pop();
                res[prev] = nums[idx];
            }

            if (i < n) {
                stack.push(idx);
            }
        }
        return res;
    }
}
