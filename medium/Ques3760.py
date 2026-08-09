# 3760. Maximum Substrings With Distinct Start
# in python
class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))

# in java
class Solution {
    public int maxDistinct(String s) {
        Set<Character> set = new HashSet<>();

        for (char ch : s.toCharArray())
            set.add(ch);

        return set.size();
    }
}
