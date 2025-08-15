// 1365. How Many Numbers Are Smaller Than the Current Number
// in java
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] arr = new int[nums.length];
        int ind = 0;
        for (int n : nums) {
            int c = 0;
            for (int i = 0; i < nums.length; i++) {
                if (n > nums[i])
                    c++;
            }
            arr[ind++] = c;
        }
        return arr;
    }
}

// in python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            c = 0
            for j in range(len(nums)):
                if i > nums[j]:
                    c += 1
            l.append(c)
        return l
