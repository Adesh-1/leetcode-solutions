# 89. Gray Code
# in python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
    
        for i in range(1 << n):   # 2^n numbers
            gray = i ^ (i >> 1)
            result.append(gray)
        
        return result

# in java
class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < (1 << n); i++) {       # // 1<<n = 2ⁿ
            int grey = i ^ (i >> 1);
            res.add(grey);
        }

        return res;
    }
}
