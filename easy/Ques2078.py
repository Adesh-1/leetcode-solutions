# 2078. Two Furthest Houses With Different Colors
# in python
class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        max_dist = 0

        # Compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = i
                break

        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                break

        return max_dist

# in java
class Solution {
    public int maxDistance(int[] colors) {
        int n = colors.length;

        int left = 0, right = n - 1;

        while (colors[left] == colors[n - 1])
            left++;
        while (colors[right] == colors[0])
            right--;

        return Math.max(n - 1 - left, right);
    }
}
