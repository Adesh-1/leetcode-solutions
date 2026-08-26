// 2904. Shortest and Lexicographically Smallest Beautiful String
// in python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        for length in range(k, n + 1):
            ans = ""

            for end in range(length, n + 1):
                temp = s[end - length : end]

                if temp.count("1") == k:
                    ans = min(ans, temp) if ans else temp

            if ans:
                return ans

        return ""

// in java
class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        int n = s.length();

        for (int a = k; a <= n; a++) {
            String ans = "";
            
            for (int b = a; b <= n; b++) {
                String temp = s.substring(b - a, b);

                // for counting 1's in substring
                int count = 0;
                for (int c = 0; c < temp.length(); c++)
                    count += temp.charAt(c) - '0';

                if ((ans.isEmpty() || temp.compareTo(ans) < 0) && count == k)
                    ans = temp;
            }
            if (!ans.isEmpty())
                return ans;
        }
        return "";
    }
}
