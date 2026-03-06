# 1784. Check if Binary String Has at Most One Segment of Ones
# in python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s

# in java
class Solution {
    public boolean checkOnesSegment(String s) {
        return !s.contains("01");
    }
}
