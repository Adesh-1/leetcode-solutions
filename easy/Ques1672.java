// 1672. Richest Customer Wealth
// in python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0 // py me aisa koi method nahi hai Min value set karne ka
        for i in range(len(accounts)):
            if richest < sum(accounts[i]):
                richest = sum(accounts[i])
        return richest

  // in java
  class Solution {
    public int maximumWealth(int[][] accounts) {
        int richest = Integer.MIN_VALUE;
        for(int i = 0; i < accounts.length; i++){
            int sum = 0;
            for(int j = 0; j < accounts[i].length; j++){
               sum += accounts[i][j];
            }
            if(richest < sum)
                richest = sum;
        }
        return richest;
    }
}
