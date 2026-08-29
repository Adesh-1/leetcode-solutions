# 1636. Sort Array by Increasing Frequency
# in python
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums

# in java
class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        Integer[] arr = new Integer[nums.length];

        for (int i = 0; i < nums.length; i++) {
            arr[i] = nums[i];
        }

        Arrays.sort(arr, (a, b) -> {        // same as python
            if (freq.get(a) != freq.get(b)) {
                return freq.get(a) - freq.get(b);
            }
            return b - a;
        });

        for (int i = 0; i < nums.length; i++) {
            nums[i] = arr[i];
        }

        return nums;
    }
}
