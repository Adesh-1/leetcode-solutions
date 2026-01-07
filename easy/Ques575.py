# 575. Distribute Candies
# in python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = len(set(candyType))
        max_candies = len(candyType) // 2
        return min(unique_types, max_candies)

# in java
class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> s = new HashSet<>();
        for (int c : candyType)
            s.add(c);
        int maxCandies = candyType.length / 2;
        return Math.min(s.size(), maxCandies);
    }
}
