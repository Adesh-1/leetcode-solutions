# 378. Kth Smallest Element in a Sorted Matrix
# in python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for i in matrix:
            for value in i:
                l.append(value)
        l.sort()
        return l[k - 1]

# in java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int low = matrix[0][0];
        int high = matrix[n - 1][n - 1];
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (countLessEqual(matrix, mid) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }
    
    private int countLessEqual(int[][] matrix, int target) {
        int n = matrix.length;
        int count = 0;
        int row = 0, col = n - 1;
        
        while (row < n && col >= 0) {
            if (matrix[row][col] <= target) {
                count += (col + 1);
                row++;
            } else {
                col--;
            }
        }
        
        return count;
    }
}
