# 2144. Minimum Cost of Buying Candies With Discount
# class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        ans = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                ans += cost[i]   # skip every 3rd candy

        return ans

# in java
class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int ans = 0;
        # // Traverse from largest to smallest
        for (int i = cost.length - 1, count = 1; i >= 0; i--, count++) {
            if (count % 3 != 0)   # // every 3rd candy is free
                ans += cost[i]; 
        }
        return ans;
    }
}
