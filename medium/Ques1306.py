# 1306. Jump Game III
# in python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(i):
            # out of bounds
            if i < 0 or i >= len(arr):
                return False

            # already visited
            if i in visited:
                return False

            # reached value 0
            if arr[i] == 0:
                return True

            visited.add(i)

            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
