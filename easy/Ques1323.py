# 1323. Maximum 69 Number
# in python
class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))

# in java
class Solution {
    public int maximum69Number(int num) {
        int n = num;
        List<Integer> l = new ArrayList<>();
        # // Convert number -> list of digits (natural order)
        while (n != 0) {
            int r = n % 10;
            l.add(0, r); #// insert at front to keep natural order
            n /= 10;
        }
        # // replace 6 --> 9
        for (int i = 0; i < l.size(); i++) {
            if (l.get(i) == 6){
                l.set(i, 9); 
                break;
            }     
        }
        # // Convert list of digits -> number
        int d = 0;
        for (int i : l)
            d = d * 10 + i;
        return d;
    }
}
