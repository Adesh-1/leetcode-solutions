# 75. Sort Colors
# in python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = Counter(nums)
        while count:
            num = min(count)
            val = count[num]
            while val:
                nums[i] = num
                i += 1
                val -= 1
            del count[num]


# in java
class Solution {
    public void sortColors(int[] nums) {
        # // bubble sort
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
    }
}
