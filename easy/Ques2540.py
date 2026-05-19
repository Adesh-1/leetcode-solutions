# 2540. Minimum Common Value
# in python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1).intersection(set(nums2))
        if not s:
            return -1
        return min(s)
