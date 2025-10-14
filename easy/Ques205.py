# 205. Isomorphic Strings
# in python

# 1st method
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        return len(set(s)) == len(set(zip(s, t)))

# 2nd method
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return [s.index(i) for i in s] == [t.index(i) for i in t]
