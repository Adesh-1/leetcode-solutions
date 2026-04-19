 // 1855. Maximum Distance Between a Pair of Values
 // in java
class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        int ans = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] <= nums2[j]) {
                ans = Math.max(ans, j - i);
                j++;
            } else {
                i++;
            }        
        }
        return ans;
    }
}

// in python
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        ans = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans
