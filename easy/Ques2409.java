// 2409. Count Days Spent Together
// in java
class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int aStart = countDays(arriveAlice);
        int aEnd = countDays(leaveAlice);
        int bStart = countDays(arriveBob);
        int bEnd = countDays(leaveBob);

        int start = Math.max(aStart, bStart);
        int end = Math.min(aEnd, bEnd);

        if (start > end)
            return 0;

        return end - start + 1;
    }

    private int countDays(String date) {
        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3));

        int[] days = { 31, 28, 31, 30, 31, 30, 
                        31, 31, 30, 31, 30, 31 };

        int total = day;

        for (int i = 0; i < month - 1; i++)
            total += days[i];

        return total;
    }
}

// in python
class Solution:
    def count_days(self, date: str) -> int:
        month, day = int(date[:2]), int(date[3:])
        total = day

        days = [31, 28, 31, 30, 31,
                 30, 31, 31, 30, 31, 30, 31]

        for i in range(month - 1):
            total += days[i]

        return total

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a_start = self.count_days(arriveAlice)
        a_end = self.count_days(leaveAlice)
        b_start = self.count_days(arriveBob)
        b_end = self.count_days(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        if start > end:
            return 0

        return end - start + 1
