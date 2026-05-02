// 788. Rotated Digits
// in python
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n + 1):
            s = str(num)
            valid = True
            changed = False
            for ch in s:
                if ch in "347":
                    valid = False
                    break

                if ch in "2569":
                    changed = True

            if valid and changed:
                count += 1

        return count

// in java
class Solution {
    public int rotatedDigits(int n) {
        int count = 0;

        for (int num = 1; num <= n; num++) {
            String s = String.valueOf(num);

            boolean valid = true;
            boolean changed = false;

            for (char ch : s.toCharArray()) {

                // invalid digits after rotation
                if (ch == '3' || ch == '4' || ch == '7') {
                    valid = false;
                    break;
                }

                // digits that change after rotation
                if (ch == '2' || ch == '5' || ch == '6' || ch == '9') {
                    changed = true;
                }
            }

            if (valid && changed) {
                count++;
            }
        }

        return count;
    }
}
