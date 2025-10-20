# 2011. Final Value of Variable After Performing Operations
# in python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if "+" in i:
                x += 1
            else:
                x -= 1
        return x

# in java
class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for (String s : operations) {
            if (s.contains("+"))
                x++;
            else
                x--;
        }
        return x;
    }
}
