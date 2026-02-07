# 1653. Minimum Deletions to Make String Balanced
# in python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                bCount += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, bCount)

        return deletions

# in java
class Solution {
    public int minimumDeletions(String s) {
        int bc = 0; # // bc = bCount
        int del = 0;
        for (char c : s.toCharArray()) {
            if (c == 'b')
                bc++;
            else
                del = Math.min(del + 1, bc);
        }
        return del;
    }
}
