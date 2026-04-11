# 3741. Minimum Distance Between Three Equal Elements II
# in python
from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)

        # Step 1: store indices
        for i, num in enumerate(nums):
            index_map[num].append(i)

        ans = float('inf')

        # Step 2: check each number
        for indices in index_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    first = indices[i]
                    last = indices[i + 2]

                    dist = 2 * (last - first)
                    ans = min(ans, dist)

        return -1 if ans == float('inf') else ans

# in java
class Solution {
    public int minimumDistance(int[] nums) {
        # // Step 1: store indices
        Map<Integer, List<Integer>> indexMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            indexMap.putIfAbsent(nums[i], new ArrayList<>());
            indexMap.get(nums[i]).add(i);
        }

        int ans = Integer.MAX_VALUE;

        # // Step 2: check each number
        for (List<Integer> indices : indexMap.values()) {
            if (indices.size() >= 3) {
                for (int i = 0; i < indices.size() - 2; i++) {
                    int first = indices.get(i);
                    int last = indices.get(i + 2);

                    int dist = 2 * (last - first);
                    ans = Math.min(ans, dist);
                }
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
