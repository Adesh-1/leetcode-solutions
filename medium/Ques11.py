# 11. Container With Most Water
# in python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxArea = 0, len(height) - 1, 0
        while left < right:
            weight = right - left
            currArea = weight * min(height[left], height[right])
            maxArea = max(maxArea, currArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

# in java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            int weight = right - left;
            int currArea = weight * Math.min(height[left], height[right]);
            maxArea = Math.max(maxArea, currArea);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return maxArea;
    }
}
