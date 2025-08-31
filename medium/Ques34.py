# 34. Find First and Last Position of Element in Sorted Array
# in python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        # find first occurrence
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
                break
        # find last occurrence
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                l.append(i)
                break
        # return [-1, -1] if target not found
        if not l:
            return [-1, -1]
        return l

# in java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] arr = new int[2];
        arr[0] = arr[1] = -1;
        int l = nums.length;
        // find first occurrence
        for (int i = 0; i < l; i++) {
            if (nums[i] == target) {
                arr[0] = i;
                break;
            }
        }
        // find last occurrence
        for (int i = l - 1; i > -1; i--) {
            if (nums[i] == target) {
                arr[1] = i;
                break;
            }
        }
        // return [-1, -1] if target not found
        if (arr[0] == -1 && arr[1] == -1)
            return arr;
        return arr;
    }
}
