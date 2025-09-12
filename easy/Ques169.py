# 169. Majority Element
# in pyhton
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = len(nums)
        for i in d:
            if d[i] > n // 2:
                return i
        return -1

  # in java
  class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return(nums[(nums.length)/2]);
    }
}
