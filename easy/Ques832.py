# 832. Flipping an Image
# in py
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Loop through each row of the matrix
        for row in image:
            # Step 1: Flip the row horizontally
            row.reverse()  # e.g., [1,1,0] -> [0,1,1]
            
            # Step 2: Invert each element in the row (0->1, 1->0)
            for i in range(len(row)):
                row[i] ^= 1  # XOR with 1 flips the bit
        return image

  # in java
  class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int row[] : image) {
            int n = image.length;
            // for reverse
            for (int i = 0; i < n / 2; i++) {
                int temp = row[i];
                row[i] = row[n - i - 1];
                row[n - i - 1] = temp;
            }
            // for invert
            for (int j = 0; j < n; j++) {
                row[j] ^= 1;
            }
        }
        return image;
    }
}
