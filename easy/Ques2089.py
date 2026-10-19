# 2089. Find Target Indices After Sorting Array
# in python
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)

        return ans

# in java
class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int less = 0, equal = 0;

        for (int num : nums) {
            if (num < target)
                less++;
            else if (num == target)
                equal++;
        }

        List<Integer> ans = new ArrayList<>();
        for (int i = less; i < less + equal; i++)
            ans.add(i);

        return ans;
    }
}
