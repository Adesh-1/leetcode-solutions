# 275. H-Index II
# in python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        h = 0
        for i in range(n):
            # papers from i to end = n - i
            papers = n - i
            if citations[i] >= papers:
                h = papers
                break
        return h

# in java
class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            int paper = n - i;
            if (citations[i] >= paper)
                return paper;
        }
        return 0;
    }
}
