// 732. My Calendar III
// in java
class MyCalendarThree {
    Map<Integer, Integer> map;
    int max;

    public MyCalendarThree() {
        map = new TreeMap<>();
        max = 0;
    }

    public int book(int startTime, int endTime) {
        int currMax = 0;

        map.put(startTime, map.getOrDefault(startTime, 0) + 1);
        map.put(endTime, map.getOrDefault(endTime, 0) - 1);

        for (int count : map.values()) {
            currMax += count;
            max = Math.max(max, currMax);
        }

        return max;
    }
}

// in python
class MyCalendarThree:

    def __init__(self):
        self.map = {}
        self.maxi = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.map[startTime] = self.map.get(startTime, 0) + 1
        self.map[endTime] = self.map.get(endTime, 0) - 1

        curr = 0

        for time in sorted(self.map):
            curr += self.map[time]
            self.maxi = max(self.maxi, curr)

        return self.maxi
