// 4. Median of Two Sorted Arrays
// in java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[] arr = new int[m + n];
        // add nums1 in arr
        for (int i = 0; i < m; i++)
            arr[i] = nums1[i];
        // add nums2 in arr
        for (int i = 0; i < n; i++)
            arr[m + i] = nums2[i];
        // sort array 'arr'
        Arrays.sort(arr);
        int len = arr.length; // find length of final array
        int mid = len / 2;  // find mid index for both conditions (even or odd)
        if (len % 2 != 0) // for even
            return arr[mid];
        else    // for odd
            return (arr[mid - 1] + arr[mid]) / 2.0; 
    }
}

// in python 3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        mid = l // 2
        if l % 2 != 0:
            return nums1[mid]
        return (nums1[mid - 1] + nums1[mid]) / 2

// in python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        mid = l // 2
        if l % 2 != 0:
            return nums1[mid]
        return (nums1[mid - 1] + nums1[mid]) / 2.0
