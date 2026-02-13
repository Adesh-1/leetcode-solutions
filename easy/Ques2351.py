# 2351. First Letter to Appear Twice
# in python
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hs = set()
        for i in s:
            if i in hs:
                return i
            else:
                hs.add(i)

# in java
class Solution {
    public char repeatedCharacter(String s) {
        Set<Character> set = new HashSet<>();
        for (char ch : s.toCharArray()) {
            if (set.contains(ch))
                return ch;
            else
                set.add(ch);
        }
        return ' ';
    }
}
