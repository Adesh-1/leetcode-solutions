# 2287. Rearrange Characters to Make Target String
# in python
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c, d = Counter(s), Counter(target)
        count = float('inf')
        for ch in d:
            count = min(count, c[ch] // d[ch])
        return count

# in java
class Solution {
    public int rearrangeCharacters(String s, String target) {
        int[] f1 = new int[26];
        int[] f2 = new int[26];
        for (char ch : s.toCharArray())
            f1[ch - 'a']++;
        for (char ch : target.toCharArray())
            f2[ch - 'a']++;

        int count = Integer.MAX_VALUE;
        for (int i = 0; i < target.length(); i++) {
            int ch = target.charAt(i);
            count = Math.min(count, f1[ch - 'a'] / f2[ch - 'a']);
        }
        return count;
    }
}
