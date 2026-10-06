# 729. My Calendar I
# in python
class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.booking:
            if start < endTime and startTime < end:
                return False

        self.booking.append([startTime, endTime])
        return True

# in java
class MyCalendar {

    List<int[]> booking;

    public MyCalendar() {
        booking = new ArrayList<>();
    }

    public boolean book(int startTime, int endTime) {
        for (int[] event : booking)
            if (event[0] < endTime && startTime < event[1])
                return false;

        booking.add(new int[] { startTime, endTime });
        return true;
    }
}
