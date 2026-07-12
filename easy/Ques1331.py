# 1331. Rank Transform of an Array
# in python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        r = 1
        for num in sorted(set(arr)):
            rank[num] = r
            r += 1
        return [rank[i] for i in arr]
      
# in java
class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] sorted = arr.clone();
        Arrays.sort(sorted);

        Map<Integer, Integer> rank = new HashMap<>();
        int r = 1;

        for (int num : sorted)
            if (!rank.containsKey(num))
                rank.put(num, r++);

        for (int i = 0; i < arr.length; i++)
            arr[i] = rank.get(arr[i]);

        return arr;
    }
}
