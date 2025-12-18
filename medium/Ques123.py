# 123. Best Time to Buy and Sell Stock III
# in python
class Solution:
    def maxProfit(self, prices):
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)

        return sell2

# in java
class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MIN_VALUE;
        int buy2 = Integer.MIN_VALUE;
        int sell1 = 0, sell2 = 0;

        for (int p : prices) {
            buy1 = Math.max(buy1, -p);          # // first buy
            sell1 = Math.max(sell1, buy1 + p);  # // first sell
            buy2 = Math.max(buy2, sell1 - p);   # // second buy
            sell2 = Math.max(sell2, buy2 + p);  # // second sell
        }

        return sell2;
    }
}
