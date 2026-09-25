# 4024. Nearest Available Drone
# in python
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min_dist = float("inf")
        ind = -1

        for i, d in enumerate(drones):
            dist = abs(d[0] - target[0]) + abs(d[1] - target[1])

            if dist <= d[2] and min_dist > dist:
                min_dist = dist
                ind = i

        return ind

# in java
class Solution {
    public int nearestDrone(int[][] drones, int[] target) {
        int minDist = Integer.MAX_VALUE;
        int ind = -1;
        int i = 0;

        for (int[] d : drones) {
            int dist = Math.abs(d[0] - target[0]) + Math.abs(d[1] - target[1]);

            if (dist <= d[2] && minDist > dist) {
                minDist = dist;
                ind = i;
            }
            i++;
        }
        return ind;
    }
}
