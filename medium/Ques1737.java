// 1737. Change Minimum Characters to Satisfy One of Three Conditions
// in java
class Solution {
    public int minCharacters(String a, String b) {
        int[] fa = new int[26];
        int[] fb = new int[26];

        for (char ch : a.toCharArray())
            fa[ch - 'a']++;

        for (char ch : b.toCharArray())
            fb[ch - 'a']++;

        int ans = a.length() + b.length();

        for (int i = 0; i < 26; i++) {

            // Condition 3:
            // Make both strings contain only character i
            int same = a.length() - fa[i] + b.length() - fb[i];
            ans = Math.min(ans, same);

            // Conditions 1 and 2
            if (i == 25)
                continue;

            int aLess = 0;
            int bLess = 0;

            for (int j = 0; j <= i; j++) {
                aLess += fa[j];
                bLess += fb[j];
            }

            // a < b
            int op1 = (a.length() - aLess) + bLess;

            // b < a
            int op2 = (b.length() - bLess) + aLess;

            ans = Math.min(ans, Math.min(op1, op2));
        }

        return ans;
    }
}

// in python
from collections import Counter

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        fa = Counter(a)
        fb = Counter(b)

        ans = len(a) + len(b)

        for i in range(26):
            ch = chr(ord('a') + i)

            same = (len(a) - fa[ch]) + (len(b) - fb[ch])
            ans = min(ans, same)

            if i == 25:
                continue

            aLess = 0
            bLess = 0

            for j in range(i + 1):
                c = chr(ord('a') + j)
                aLess += fa[c]
                bLess += fb[c]

            op1 = (len(a) - aLess) + bLess
            op2 = (len(b) - bLess) + aLess

            ans = min(ans, op1, op2)

        return ans
