# 118. Pascal's Triangle
# in python
class Solution:
    def generate(self, numRows: int):
        result = list()  # can write l1=[]

        for i in range(numRows):
            row = list()  # can write l2=[]
            m = 1

            for j in range(i + 1):
                row.append(m)
                m = (m * (i - j)) // (j + 1)

            result.append(row)

        return result

# in java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            long m = 1;

            for (int j = 0; j <= i; j++) {
                row.add((int) m);
                m = (m * (i - j)) / (j + 1);
            }

            result.add(row);
        }

        return result;
    }
}
