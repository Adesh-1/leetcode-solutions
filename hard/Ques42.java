// 42. Trapping Rain Water
// in java
class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] right = new int[n];

        // for right boundary
        right[0] = height[0];
        for (int i = 1; i < n; i++)
            right[i] = Math.max(right[i - 1], height[i]);

        int[] left = new int[n];
        
        // for left boundary
        left[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            left[i] = Math.max(left[i + 1], height[i]);
        }

        int trapped_water = 0;
        for (int i = 0; i < n; i++) {
            int waterLevel = Math.min(left[i], right[i]);
            trapped_water += waterLevel - height[i];
        }
        return trapped_water;
    }
}
