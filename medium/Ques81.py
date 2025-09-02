# 81. Search in Rotated Sorted Array II
# in py
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

  # in java
  class Solution {
    public boolean search(int[] nums, int target) {
        for (int i : nums) {
            if (i == target)
                return true;
        }
        return false;
    }
}
