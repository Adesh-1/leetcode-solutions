# 90. Subsets II
# in python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = [[]]
        last_size = 0

        for i in range(len(nums)):
            start = 0

            if i > 0 and nums[i] == nums[i - 1]:
                start = last_size

            last_size = len(result)

            for j in range(start, last_size):
                result.append(result[j] + [nums[i]])

        return result

# in java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());

        int lastSize = 0;

        for (int i = 0; i < nums.length; i++) {
            int start = 0;

            if (i > 0 && nums[i] == nums[i - 1]) {
                start = lastSize;
            }

            lastSize = result.size();

            for (int j = start; j < lastSize; j++) {
                List<Integer> subset = new ArrayList<>(result.get(j));
                subset.add(nums[i]);
                result.add(subset);
            }
        }

        return result;
    }
}
