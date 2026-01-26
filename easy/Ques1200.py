# 1200. Minimum Absolute Difference
# in python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')

        # First pass: find minimum difference
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])

        result = []

        # Second pass: collect pairs
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result

# in java
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);

        int minDiff = Integer.MAX_VALUE;

        # // First pass: find minimum difference
        for (int i = 0; i < arr.length - 1; i++) {
            minDiff = Math.min(minDiff, arr[i + 1] - arr[i]);
        }

        List<List<Integer>> result = new ArrayList<>();

        # // Second pass: collect pairs with minDiff
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] - arr[i] == minDiff) {
                result.add(Arrays.asList(arr[i], arr[i + 1]));
            }
        }

        return result;
    }
}
