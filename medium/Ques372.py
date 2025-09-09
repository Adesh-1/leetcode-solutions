# 372. Super Pow
# in python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        p = int("".join(str(i) for i in b))
        return pow(a, p, 1337)

  
