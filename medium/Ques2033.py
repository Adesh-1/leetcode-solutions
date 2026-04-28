# 2033. Minimum Operations to Make a Uni-Value Grid
# in python
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []

        # Flatten grid
        for row in grid:
            for num in row:
                arr.append(num)

        # Check if possible
        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1

        # Sort and take median
        arr.sort()
        median = arr[len(arr) // 2]

        # Count operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x

        return ops


# in java
class Solution {
    public int minOperations(int[][] grid, int x) {
        List<Integer> arr = new ArrayList<>();

        # // Flatten grid
        for (int[] row : grid) {
            for (int num : row) {
                arr.add(num);
            }
        }

        # // Check if possible
        int rem = arr.get(0) % x;

        for (int num : arr) {
            if (num % x != rem) {
                return -1;
            }
        }

        # // Sort and median
        Collections.sort(arr);
        int median = arr.get(arr.size() / 2);

        # // Count operations
        int ops = 0;

        for (int num : arr) {
            ops += Math.abs(num - median) / x;
        }

        return ops;
    }
}
