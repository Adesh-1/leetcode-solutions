# 1828. Queries on Number of Points Inside a Circle
# in python
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        answer = []

        for cx, cy, r in queries:
            count = 0

            for px, py in points:
                distance_squared = (px - cx) ** 2 + (py - cy) ** 2

                if distance_squared <= r ** 2:
                    count += 1

            answer.append(count)

        return answer

# in java
class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] ans = new int[queries.length];
        int i = 0;

        for (int[] center : queries) {
            int cx = center[0];
            int cy = center[1];
            int r = center[2];

            int count = 0;

            for (int[] point : points) {
                int px = point[0];
                int py = point[1];

                int distance = (px - cx) * (px - cx) + (py - cy) * (py - cy);

                if (distance <= r * r)
                    count++;
            }
            ans[i++] = count;
        }
        return ans;
    }
}
