// 594. Longest Harmonious Subsequence
// in java
class Solution {
    public int findLHS(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        // Count frequency
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int maxLen = 0;
        // Check pairs
        for (int key : map.keySet()) {
            if (map.containsKey(key + 1))
                maxLen = Math.max(maxLen, map.get(key) + map.get(key + 1));
        }
        return maxLen;
    }
}

// in python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len
