# 88. Merge Sorted Array
# in pyhton
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()

  # in java
  class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int total_len = m + n;
        for (int i = m; i < total_len; i++) {
            nums1[i] = nums2[i-m];
        }
        Arrays.sort(nums1);
    }
}
