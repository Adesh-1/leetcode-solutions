# 658. Find K Closest Elements
# in python
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - 1

        # shrink window until size is k
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left:right+1]

# in java
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0;
        int right = arr.length - 1;

        while (right - left + 1 > k) {
            if (Math.abs(arr[left] - x) > Math.abs(arr[right] - x))
                left++;
            else
                right--;
        }

        List<Integer> l = new ArrayList<>();
        for (int i = left; i <= right; i++)
            l.add(arr[i]);

        return l;
    }
}
