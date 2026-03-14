# 1009. Complement of Base 10 Integer
# in python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = f"{n:b}"
        b = "".join("1" if c == "0" else "0" for c in b)
        return int(b, 2)
