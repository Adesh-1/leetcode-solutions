// 525. Contiguous Array
// in python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        sum = max_len = 0

        for i, num in enumerate(nums):
            sum += -1 if num == 0 else 1

            if sum in map:
                length = i - map[sum]
                max_len = max(max_len, length)
            else:
                map[sum] = i

        return max_len

// in java
  class Solution {
    public int findMaxLength(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        // prefix sum 0 exists before the array starts
        map.put(0, -1);

        int sum = 0;
        int maxLen = 0;

        for (int i = 0; i < nums.length; i++) {

            // 0 -> -1
            // 1 -> +1
            if (nums[i] == 0) {
                sum--;
            } else {
                sum++;
            }

            // Same prefix sum already seen
            if (map.containsKey(sum)) {
                int len = i - map.get(sum);
                maxLen = Math.max(maxLen, len);
            } 
            else {
                // Store only the FIRST occurrence
                map.put(sum, i);
            }
        }

        return maxLen;
    }
}
