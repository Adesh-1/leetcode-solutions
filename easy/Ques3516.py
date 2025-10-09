# 3516. Find Closest Person
# in python
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x - z), abs(y - z)
        if d1 == d2:
            return 0
        per = 1 if d1 < d2 else 2
        return per

  # in java
  class Solution {
    public int findClosest(int x, int y, int z) {
        int d1 = Math.abs(x - z);
        int d2 = Math.abs(y - z);
        if (d1 == d2)
            return 0;
        int per = d1 < d2 ? 1 : 2;
        return per;
    }
}
