# 2110. Number of Smooth Descent Periods of a Stock
# in python
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        curr = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1
            ans += curr

        return ans

# in java
class Solution {
    public long getDescentPeriods(int[] prices) {
        int curr = 1;
        long ans = 1;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] == prices[i - 1] - 1)
                curr++;
            else
                curr = 1;
            ans += curr;
        }
        return ans;
    }
}
