# 1525. Number of Good Ways to Split a String
# in python
class Solution:
    def numSplits(self, s: str) -> int:
        left, right = set(), set(s)
        freq = Counter(s)
        ans = 0
        for i in range(len(s) - 1):
            ch = s[i]
            left.add(ch)

            freq[ch] -= 1

            if freq[ch] == 0:
                right.remove(ch)

            if len(left) == len(right):
                ans += 1

        return ans

# in java
class Solution {
    public int numSplits(String s) {
        Set<Character> left = new HashSet<>();
        Set<Character> right = new HashSet<>();
        Map<Character, Integer> freq = new HashMap<>();

        for (Character ch : s.toCharArray()) {
            right.add(ch);
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }

        int ans = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            char ch = s.charAt(i);
            left.add(ch);

            freq.put(ch, freq.get(ch) - 1);
            if (freq.get(ch) == 0)
                right.remove(ch);

            if (left.size() == right.size())
                ans++;
        }
        return ans;
    }
}
