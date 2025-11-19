// 2154. Keep Multiplying Found Values by Two
// in java
    // using HashSet
class Solution {
    public int findFinalValue(int[] nums, int original) {
        // create set
        Set<Integer> set = new HashSet<>();
        for (int n : nums)
            set.add(n);
        // double the no while no is in set
        while (set.contains(original))
            original *= 2;

        return original;
    }
}

  // sorting the array
class Solution {
    public int findFinalValue(int[] nums, int original) {
        // sort the array
        Arrays.sort(nums);
        // checks the no in the array
        for (int i = 0; i < nums.length; i++) {
            // if found then double it and check again
            if (nums[i] == original)
                original *= 2;
        }
        return original;
    }
}

// in python
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original
