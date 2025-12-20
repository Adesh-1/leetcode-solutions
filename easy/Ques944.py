# 944. Delete Columns to Make Sorted
# in python
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0

        for c in range(cols):
            for r in range(rows - 1):
                if strs[r][c] > strs[r + 1][c]:
                    delete_count += 1
                    break   # no need to check further rows for this column

        return delete_count

# in java
class Solution {
    public int minDeletionSize(String[] strs) {
        int rows = strs.length;
        int cols = strs[0].length();
        int deleteCount = 0;

        for (int c = 0; c < cols; c++) {
            for (int r = 0; r < rows - 1; r++) {
                if (strs[r].charAt(c) > strs[r + 1].charAt(c)) {
                    deleteCount++;
                    break; # // stop checking this column
                }
            }
        }
        return deleteCount;
    }
}
