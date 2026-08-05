# 1817. Finding the Users Active Minutes
# in python
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mp = defaultdict(set)

        for user, minutes in logs:
            mp[user].add(minutes)

        ans = [0] * k

        for minutes in mp.values():
            ans[len(minutes) - 1] += 1

        return ans

# in java
class Solution {
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        HashMap<Integer, HashSet<Integer>> map = new HashMap<>();

        for (int[] log : logs) {
            map.putIfAbsent(log[0], new HashSet<>());
            map.get(log[0]).add(log[1]);
        }

        int[] ans = new int[k];

        for (HashSet<Integer> set : map.values())
            ans[set.size() - 1]++;

        return ans;
    }
}
