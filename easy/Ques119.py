# 119. Pascal's Triangle II
# in python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = list()  # can write l1=[]
        for i in range(rowIndex+1):
            row = list()  # can write l2=[]
            m = 1
            for j in range(i + 1):
                row.append(m)
                m = (m * (i - j)) // (j + 1)
            result.append(row)
        return result[rowIndex]

# in java
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        long val = 1;

        for (int i = 0; i <= rowIndex; i++) {
            row.add((int) val);
            val = val * (rowIndex - i) / (i + 1);
        }
        return row;
    }
}
