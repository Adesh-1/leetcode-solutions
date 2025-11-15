# 1441. Build an Array With Stack Operations
# in python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l, last = [], target[-1]
        s = set(target)     # for better time complexity
        for i in range(1, last + 1):
            l.append("Push")
            if i not in s:
                l.append("Pop")
        return l

# in java
class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> result = new ArrayList<>();
        int idx = 0;

        for (int i = 1; i <= target[target.length - 1]; i++) {
            result.add("Push");

            if (i == target[idx]) {
                idx++;  // matches desired number
            } else {
                result.add("Pop"); // extra number, remove it
            }
        }
        return result;
    }
}
