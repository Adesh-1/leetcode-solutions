# 386. Lexicographical Numbers
# in python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)

# in java
class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> result = new ArrayList<>();
        int num = 1;
        
        for (int i = 0; i < n; i++) {
            result.add(num);
            
            if (num * 10 <= n) {
                // Go deeper: multiply by 10
                num *= 10;
            } else {
                // If cannot go deeper, go to next number
                while (num % 10 == 9 || num + 1 > n) {
                    num /= 10;  // backtrack
                }
                num++;
            }
        }
        
        return result;
    }
}
