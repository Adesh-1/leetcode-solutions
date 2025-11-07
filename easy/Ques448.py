# 448. Find All Numbers Disappeared in an Array
# in python

# 1st method
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d, s = list(), set(nums)
        for i in range(1, len(nums) + 1):
            if i not in s:
                d.append(i)
        return d

# 2nd method
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = [i for i in range(1, len(nums) + 1)]
        d, nums = list(), set(nums)
        for i in l:
            if i not in nums:
                d.append(i)
        return d

# 3rd method
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = set([i for i in range(1, len(nums) + 1)])
        d = list(set(l).difference(set(nums)))
        return d
