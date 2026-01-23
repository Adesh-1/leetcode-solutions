# 2210. Count Hills and Valleys in an Array
# in python
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # remove consecutive duplicates
        l = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                l.append(nums[i])

        # count hills and valleys
        n = 0
        for i in range(1, len(l) - 1):
            if l[i - 1] < l[i] > l[i + 1]:  # for count hills
                n += 1
            elif l[i - 1] > l[i] < l[i + 1]: # for count valleys
                n += 1
        return n

# in java
class Solution {
    public int countHillValley(int[] nums) {
        # // Step 1: remove consecutive duplicates
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(nums[0]);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                arr.add(nums[i]);
            }
        }

        # // Step 2: count hills and valleys
        int count = 0;

        for (int i = 1; i < arr.size() - 1; i++) {
            int prev = arr.get(i - 1);
            int curr = arr.get(i);
            int next = arr.get(i + 1);

            # // hill
            if (curr > prev && curr > next) {
                count++;
            }
            # // valley
            else if (curr < prev && curr < next) {
                count++;
            }
        }

        return count;
    }
}
