# 3551. Minimum Swaps to Sort by Digit Sum
# in python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        digit_sum = lambda num: sum(map(int, str(num)))

        rank = {x: k for k, x in enumerate(sorted(nums, key=lambda x: (digit_sum(x), x)))}

        ind = [rank[num] for num in nums]
        swaps = 0

        for i in range(len(ind)):
            while ind[i] != i:
                j = ind[i]
                ind[i], ind[j] = ind[j], ind[i]
                swaps += 1

        return swaps

# in java
class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;

        Integer[] sorted = new Integer[n];
        for (int i = 0; i < n; i++) {
            sorted[i] = nums[i];
        }

        Arrays.sort(sorted, (a, b) -> {
            int sumA = digitSum(a);
            int sumB = digitSum(b);

            if (sumA != sumB) {
                return Integer.compare(sumA, sumB);
            }
            return Integer.compare(a, b);
        });

        Map<Integer, Integer> rank = new HashMap<>();
        for (int i = 0; i < n; i++) {
            rank.put(sorted[i], i);
        }

        int[] ind = new int[n];
        for (int i = 0; i < n; i++) {
            ind[i] = rank.get(nums[i]);
        }

        int swaps = 0;

        for (int i = 0; i < n; i++) {
            while (ind[i] != i) {
                int j = ind[i];

                int temp = ind[i];
                ind[i] = ind[j];
                ind[j] = temp;

                swaps++;
            }
        }

        return swaps;
    }

    private int digitSum(int num) {
        int sum = 0;

        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }

        return sum;
    }
}
