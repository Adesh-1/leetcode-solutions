# 1207. Unique Number of Occurrences
# in python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        s = set()
        for i in d.values():
            if i in s:
                return False
            else:
                s.add(i)
        return True
