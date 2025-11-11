// 292. Nim Game
// in java
class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}

// in python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
