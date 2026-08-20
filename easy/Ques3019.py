# 3069. Distribute Elements Into Two Arrays I
# in python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1, a2 = [nums[0]], [nums[1]]

        for num in nums[2:]:
            (a1 if a1[-1] > a2[-1] else a2).append(num)

        return a1 + a2

# in java
class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();

        l1.add(nums[0]);
        l2.add(nums[1]);

        for (int i = 2; i < nums.length; i++) {
            if (l1.get(l1.size() - 1) > l2.get(l2.size() - 1))
                l1.add(nums[i]);
            else
                l2.add(nums[i]);
        }

        int[] result = new int[nums.length];
        int ind = 0;

        for (int num : l1)
            result[ind++] = num;

        for (int num : l2)
            result[ind++] = num;

        return result;
    }
}
