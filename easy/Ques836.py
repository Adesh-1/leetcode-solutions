# 836. Rectangle Overlap
# in python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return width > 0 and height > 0

# in java
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        int width = Math.min(rec1[2], rec2[2]) - Math.max(rec1[0], rec2[0]);
        int height = Math.min(rec1[3], rec2[3]) - Math.max(rec1[1], rec2[1]);

        return width > 0 && height > 0;
    }
}
