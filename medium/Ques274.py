# 274. H-Index
# in python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            paper = n - i
            if citations[i] >= paper:
                return paper
        return 0

# in java
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            int paper = n - i;
            if (citations[i] >= paper)
                return paper;
        }
        return 0;
    }
}
