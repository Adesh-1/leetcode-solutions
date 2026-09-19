# 1401. Circle and Rectangle Overlapping
# in python
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        distance = (xCenter - closestX) ** 2 + (yCenter - closestY) ** 2

        return distance<=radius**2

# in java
class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int closestX = Math.max(x1, Math.min(xCenter, x2));
        int closestY = Math.max(y1, Math.min(yCenter, y2));

        int distX = (xCenter - closestX);
        int distY = (yCenter - closestY);

        int distance = distX * distX + distY * distY;

        return distance <= radius * radius;
    }
}
