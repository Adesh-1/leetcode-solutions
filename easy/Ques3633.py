# 3633. Earliest Finish Time for Land and Water Rides I
# in python
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):

                ans = min(
                    ans,
                    max(ls + ld, ws) + wd,  # Land -> Water
                    max(ws + wd, ls) + ld   # Water -> Land
                )

        return ans

# in java
class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration,
            int[] waterStartTime, int[] waterDuration) {

        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < landStartTime.length; i++) {
            for (int j = 0; j < waterStartTime.length; j++) {

                // Land -> Water
                int landFinish = landStartTime[i] + landDuration[i];
                int finish1 = Math.max(landFinish, waterStartTime[j]) + waterDuration[j];

                // Water -> Land
                int waterFinish = waterStartTime[j] + waterDuration[j];
                int finish2 = Math.max(waterFinish, landStartTime[i]) + landDuration[i];

                ans = Math.min(ans, Math.min(finish1, finish2));
            }
        }

        return ans;
    }
}
