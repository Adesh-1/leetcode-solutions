# 283. Move Zeroes
# in pyhton
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li = -1  # index from last
        si = 0  # index from start 
        cnums = nums.copy()  # copy of nums list 
        for i in cnums:
            if i != 0:
                nums[si] = i
                si += 1
            else:
                nums[li] = i
                li -= 1

# in java
class Solution {
    public void moveZeroes(int[] nums) {
        # // int[] numsCopy = nums.clone(); // make a copy of array
        int str_ind = 0;
        for (int i : nums) {
            if (i != 0) {
                nums[str_ind] = i;
                str_ind++;
            }
        }
        while (str_ind < nums.length) {
            nums[str_ind] = 0;
            str_ind++;
        }
    }
}
