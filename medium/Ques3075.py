# 3075. Maximize Happiness of Selected Children
# in python
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0

        for i in range(k):
            ans += max(happiness[i] - i, 0)

        return ans

# in java
class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long ans = 0;
        int n = happiness.length;

        for (int i = 0; i < k; i++) {
            int val = happiness[n - 1 - i] - i;
            if (val > 0)
                ans += val;
        }
        return ans;
    }
}
