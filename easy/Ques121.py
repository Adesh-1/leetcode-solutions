# 121. Best Time to Buy and Sell Stock
# in pyhton
class Solution:
    def maxProfit(self, p: List[int]) -> int:
        profit, m = 0, p[0]   # profit = 0, m = first price
        for price in p:
            m = min(price, m)                 # track the lowest price so far
            profit = max(profit, price - m)   # check if selling today gives more profit
        return profit

  # in java
  class Solution {
    public int maxProfit(int[] p) {
        int profit = 0;
        int minPrice = p[0];
        for (int i = 0; i < p.length; i++) {
            if (p[i] < minPrice)
                minPrice = p[i];
            else if ((p[i] - minPrice) > profit)
                profit = p[i] - minPrice;
        }
        return profit;
    }
}
