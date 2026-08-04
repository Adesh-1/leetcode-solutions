# 3731. Find Missing Elements
# in python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l, s = [], set(nums)

        for i in range(min(s), max(s)):
            if i not in s:
                l.append(i)

        return l

# in java
class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Arrays.sort(nums);
        int j = 0;
        List<Integer> l = new ArrayList<>();

        for (int i = nums[0]; i < nums[nums.length - 1]; i++) {
            if (nums[j] != i)
                l.add(i);
            else
                j++;
        }
        return l;
    }
}
