# 3751. Total Waviness of Numbers in Range I
# in python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            for i in range(1, len(s) - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or \
                    (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    ans += 1
        return ans

# in java
class Solution {
    public int totalWaviness(int num1, int num2) {
        int ans = 0;
        for (int n = num1; n <= num2; n++) {
            String s = String.valueOf(n);
            for (int i = 1; i < s.length() - 1; i++) {
                char prev = s.charAt(i - 1);
                char curr = s.charAt(i);
                char next = s.charAt(i + 1);
                if ((curr > prev && curr > next) ||
                        (curr < prev && curr < next))
                    ans++;
            }
        }
        return ans;
    }
}
