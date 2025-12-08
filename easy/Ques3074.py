# 3074. Apple Redistribution into Boxes
# in python
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        box = 0
        for i in capacity:   
            s -= i
            box += 1
            if s <= 0:
                break
        return box

# in java
class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {

        int total = Arrays.stream(apple).sum();

        Arrays.sort(capacity);

        int boxes = 0;
        for (int i = capacity.length - 1; i >= 0 && total > 0; i--) {
            total -= capacity[i];
            boxes++;
        }
        return boxes;
    }
}
