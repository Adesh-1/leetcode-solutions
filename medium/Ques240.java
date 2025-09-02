// 240. Search a 2D Matrix II
// in java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int[] i : matrix){
            for(int j : i){
                if(j == target)
                    return true;
            }
        }
        return false;
    }
}

// in pyhton
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False
