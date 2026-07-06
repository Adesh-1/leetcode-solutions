# 1288. Remove Covered Intervals
# in python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = 0
        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        return count

# in java
class Solution {
    public int removeCoveredIntervals(int[][] intervals) {

        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];   // end descending
            }
            return a[0] - b[0];       // start ascending
        });

        int count = 0;
        int maxEnd = 0;

        for (int[] interval : intervals) {
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
        }

        return count;
    }
}
