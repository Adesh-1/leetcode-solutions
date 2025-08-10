// 1920. Build Array from Permutation
// in java
class Solution {
    public int[] buildArray(int[] nums) {
        int[] a = new int[nums.length];
        int ind = 0;
        for(int i : nums){
            a[ind] = nums[i];
            ind++;
        }
        return a;
    }
}

// in python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(nums[i])
        return l
