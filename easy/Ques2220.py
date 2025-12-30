# 2220. Minimum Bit Flips to Convert Number
# in python
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count("1")

# in java
class Solution {
    public int minBitFlips(int start, int goal) {
        return Integer.bitCount(start ^ goal);
    }
}
