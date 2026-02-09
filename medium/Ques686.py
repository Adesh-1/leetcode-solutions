# 686. Repeated String Match
# in python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        s = ""
        count = 0

        # Repeat until length >= b
        while len(s) < len(b):
            s += a
            count += 1

        # Check once
        if b in s:
            return count

        # One extra repeat
        s += a
        count += 1

        if b in s:
            return count

        return -1


# in java
class Solution {
    public int repeatedStringMatch(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int count = 0;

        while (sb.length() < b.length()) {
            sb.append(a);
            count++;
        }
        if (sb.indexOf(b) != -1)
            return count;

        sb.append(a);
        count++;

        if (sb.indexOf(b) != -1)
            return count;

        return -1;
    }
}
