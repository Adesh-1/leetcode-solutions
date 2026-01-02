# 961. N-Repeated Element in Size 2N Array
# in python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k, v in d.items():
            if v > 1:
                return k

# in java
class Solution {
    public int repeatedNTimes(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int key : map.keySet()) {
            if (map.get(key) > 1) {
                return key;
            }
        }
        return -1;
    }
}
