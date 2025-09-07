# 1351. Count Negative Numbers in a Sorted Matrix
# in python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_count = 0
        for row in grid:
            for val in row:
                if val < 0:
                    neg_count += 1
        return neg_count 

# in java
class Solution {
    public int countNegatives(int[][] grid) {
        int count = 0;
        for (int i[] : grid) {
            for (int j : i) {
                if (j < 0)
                    count++;
            }
        }
        return count;
    }
}
