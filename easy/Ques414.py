# 414. Third Maximum Number
# in python
# 1st method
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        l.sort(reverse=True)
        if len(l) < 3:
            return max(l)
        return l[2]

# 2nd method
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        l.sort()
        l.reverse()
        if len(l) < 3:
            return max(l)
        return l[2]
