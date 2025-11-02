# 405. Convert a Number to Hexadecimal
# in python
# 1st method
class Solution:
    def toHex(self, num: int) -> str:
        return hex(num & 0xFFFFFFFF)[2:]

# 2nd method
class Solution:
    def toHex(self, num: int) -> str:
        return f"{(num & 0xffffffff):x}"
