# 1291. Sequential Digits
# in python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = []
        s, e = len(str(low)), len(str(high))
        for i in range(s, e + 1):
            for j in range(1, 10 - i + 1):
                num = 0
                for k in range(j, j + i):
                    num = num * 10 + k
                if low <= num <= high:
                    l.append(num)
        return l

# in java
class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> l = new ArrayList<>();
        int s = String.valueOf(low).length();
        int e = String.valueOf(high).length();
        for (int i = s; i <= e; i++) {
            for (int j = 1; j <= 10 - i; j++) {
                int num = 0;
                for (int k = j; k < j + i; k++)
                    num = num * 10 + k;
                if (num >= low && num <= high)
                    l.add(num);
            }
        }
        return l;
    }
}
