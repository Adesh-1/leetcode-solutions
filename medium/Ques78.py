# 78. Subsets
# in python
class Solution:
    def subsets(self, nums):
        result = [[]]   # start with empty subset
        
        for num in nums:
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])  # add current num to each existing subset
            result += new_subsets  # add them all to the list
        
        return result

# in java
    # same approach as python code
  class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>()); // start with empty subset

        for (int num : nums) {
            List<List<Integer>> newSubsets = new ArrayList<>();
            for (List<Integer> subset : result) {
                // create a new subset by adding the current number
                List<Integer> newSubset = new ArrayList<>(subset);
                newSubset.add(num);
                newSubsets.add(newSubset);
            }
            result.addAll(newSubsets); // add all new subsets to the result
        }

        return result;
    }

    // Optional: main method to test
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1, 2, 3};
        List<List<Integer>> subsets = sol.subsets(nums);
        System.out.println(subsets);
    }
}
