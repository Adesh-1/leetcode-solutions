// 492. Construct the Rectangle
// in java
class Solution {
    public int[] constructRectangle(int area) {
        int w = (int) Math.sqrt(area);
        while (w > 0) {
            if (area % w == 0)
                return new int[] { area / w, w };
                    // here "area / w" return int because "int / int -> int"
            w--;
        }
        return new int[] { area, 1 };
    }
}

// in python
import math as m
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(m.sqrt(area))
        while w > 0:
            if area % w == 0:
                return [area // w, w]
            w -= 1
        return [area, 1]
