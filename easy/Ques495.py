# 495. Teemo Attacking
# in python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total, end = 0, 0
        for t in timeSeries:
            total += duration
            if t < end:
                overlap = end - t
                total -= overlap
            end = t + duration
        return total

# in java
class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int total = 0;
        int end = 0;
        for (int t : timeSeries) {
            total += duration;
            if (t < end) {
                int overlap = end - t;
                total -= overlap;
            }
            end = t + duration;
        }
        return total;
    }
}
