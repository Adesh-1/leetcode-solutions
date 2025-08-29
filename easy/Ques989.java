// 989. Add to Array-Form of Integer
// in java
class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        LinkedList<Integer> result = new LinkedList<>();
        int i = num.length - 1;

        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i];  // add digit from num
                i--;
            }
            result.addFirst(k % 10); // store last digit
            k /= 10;                 // carry for next round
        }

        return result;
    }
}

// in py
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = len(num) - 1
        res = []
        while l >= 0 or k > 0:
            if l >= 0:
                k += num[l]
                l -= 1
            res.append(k % 10)
            k //= 10
        return res[::-1]
