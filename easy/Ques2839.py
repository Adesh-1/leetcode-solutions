# 2839. Check if Strings Can be Made Equal With Operations I
# in python
    # 1st method
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (sorted(s1[::2]) == sorted(s2[::2]) and
                sorted(s1[1::2]) == sorted(s2[1::2]))

    # 2nd method
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (Counter(s1[::2]) == Counter(s2[::2]) and
                Counter(s1[1::2]) == Counter(s2[1::2]))

# in java
class Solution {
    public boolean canBeEqual(String s1, String s2) {
        return match(s1.charAt(0), s1.charAt(2), s2.charAt(0), s2.charAt(2)) &&
               match(s1.charAt(1), s1.charAt(3), s2.charAt(1), s2.charAt(3));
    }

    private boolean match(char a1, char a2, char b1, char b2) {
        return (a1 == b1 && a2 == b2) || (a1 == b2 && a2 == b1);
    }
}
