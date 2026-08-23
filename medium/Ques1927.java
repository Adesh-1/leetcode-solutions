// 1927. Sum Game
// in java
class Solution {
    public boolean sumGame(String num) {
        int n = num.length();

        int[] left = getInfo(num.substring(0, n / 2)); // first half
        int[] right = getInfo(num.substring(n / 2, n)); // second half

        // k = known, u = unknown(?)
        int lk = left[0], lu = left[1];
        int rk = right[0], ru = right[1];

        return (lu + ru) % 2 == 1 || lk - rk != 9 * (ru - lu) / 2;
    }

    private int[] getInfo(String s) {
        int k = 0, u = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '?')
                u++;
            else
                k += ch - '0';
        }

        return new int[] { k, u };
    }
}

// in python
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        left = self.get_info(num[:n])
        right = self.get_info(num[n:])

        lk, lu = left
        rk, ru = right

        return (lu + ru) % 2 == 1 or lk - rk != 9 * (ru - lu) // 2

    def get_info(self, s):
        k = u = 0

        for ch in s:
            if ch == "?":
                u += 1
            else:
                k += int(ch)

        return k, u
