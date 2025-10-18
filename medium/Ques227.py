# 227. Basic Calculator II
# in python
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace("/", "//")
        print(s)
        return eval(s)
