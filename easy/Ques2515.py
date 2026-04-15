# 2515. Shortest Distance to Target String in a Circular Array
# in python
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        n = len(words)
        min_dist = float('inf')

        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                dist = min(diff, n - diff)
                min_dist = min(min_dist, dist)

        return -1 if min_dist == float('inf') else min_dist

# in java
class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        int n = words.length;
        int minDist = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            if (words[i].equals(target)) {
                int diff = Math.abs(i - startIndex);
                int dist = Math.min(diff, n - diff);
                minDist = Math.min(minDist, dist);
            }
        }

        return minDist == Integer.MAX_VALUE ? -1 : minDist;
    }
}
