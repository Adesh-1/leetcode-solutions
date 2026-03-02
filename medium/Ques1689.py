# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# in python
    # 1st method
class Solution:
    def minPartitions(self, n: str) -> int:
        nl = set(int(i) for i in n)
        return max(nl)

    # 2nd method
class Solution:
    def minPartitions(self, n: str) -> int:
        for d in "987654321":
            if d in n:
                return int(d)

# in java
class Solution {
    public int minPartitions(String n) {
        int max = 0;
        for (char ch : n.toCharArray())
            max = Math.max(max, ch - '0');
        return max;
    }
}
