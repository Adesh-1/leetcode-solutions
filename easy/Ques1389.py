# 1389. Create Target Array in the Given Order
# in py
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            l.insert(index[i], nums[i])
        return l

  # in java
  class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> n = new ArrayList<>();
        int[] arr = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            n.add(index[i], nums[i]);
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = n.get(i);
        }
        return arr;
    }
}
