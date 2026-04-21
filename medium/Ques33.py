# 33. Search in Rotated Sorted Array
# in python
class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

  # in java
 class Solution {
    public int search(int[] nums, int target) {
        int si = 0;
        int ei = nums.length - 1;
        while (si <= ei) {
            int mid = si + (ei - si) / 2;

            if (nums[mid] == target)
                return mid;

            # // search on L1 
            if (nums[si] <= nums[mid]) {
                # // in left
                if (nums[si] <= target && target < nums[mid])
                    ei = mid - 1;
                # // in right
                else
                    si = mid + 1;
            }
            # // search on L2 
            else {
                # // in right
                if (nums[mid] < target && target <= nums[ei])
                    si = mid + 1;
                # // in left
                else
                    ei = mid - 1;
            }
        }
        return -1;
    }
}
