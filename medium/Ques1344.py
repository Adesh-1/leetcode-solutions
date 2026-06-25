# 1344. Angle Between Hands of a Clock
# in python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)

# in java
class Solution {
    public double angleClock(int hour, int minutes) {
        double minutesAngle = minutes * 6.0;
        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;
        double diff = Math.abs(hourAngle - minutesAngle);
        return Math.min(diff, 360.0 - diff);
    }
}
