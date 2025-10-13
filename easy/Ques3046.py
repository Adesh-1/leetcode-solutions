# 3046. Split the Array
# in python
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for value in d.values():
            if value > 2:
                return False
        return True

# in java
class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
            if (count.get(num) > 2) {
                return false;
            }
        }

        return true;
    }
}
