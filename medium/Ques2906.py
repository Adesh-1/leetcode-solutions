# 2906. Construct Product Matrix
# in python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        # Step 1: Flatten matrix
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        
        # Step 2: Prefix product
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        # Step 3: Suffix product
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # Step 4: Build result using prefix * suffix
        result = []
        for i in range(size):
            val = (prefix[i] * suffix[i]) % MOD
            result.append(val)
        
        # Step 5: Convert back to 2D
        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(result[idx])
                idx += 1
            ans.append(row)
        
        return ans

# in java
class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        int MOD = 12345;
        int n = grid.length, m = grid[0].length;
        int size = n * m;

        # // Step 1: Flatten matrix
        int[] arr = new int[size];
        int idx = 0;
        for (int[] row : grid) {
            for (int val : row) {
                arr[idx++] = val % MOD;
            }
        }

        # // Step 2: Prefix product
        int[] prefix = new int[size];
        prefix[0] = 1;
        for (int i = 1; i < size; i++) {
            prefix[i] = (int)((long)prefix[i - 1] * arr[i - 1] % MOD);
        }

        # // Step 3: Suffix product
        int[] suffix = new int[size];
        suffix[size - 1] = 1;
        for (int i = size - 2; i >= 0; i--) {
            suffix[i] = (int)((long)suffix[i + 1] * arr[i + 1] % MOD);
        }

        # // Step 4: Build result
        int[][] ans = new int[n][m];
        idx = 0;
        for (int i = 0; i < size; i++) {
            int val = (int)((long)prefix[i] * suffix[i] % MOD);
            ans[idx / m][idx % m] = val;
            idx++;
        }

        return ans;
    }
}
