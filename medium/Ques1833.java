// 1833. Maximum Ice Cream Bars
// in python
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for i in costs:
            if coins >= i:
                count += 1
                coins -= i
            else:
                break
        return count

// in java
  class Solution {
    public int maxIceCream(int[] costs, int coins) {
        // using counting sort
        int[] freq = new int[100001];

        // count frequency
        for (int cost : costs)
            freq[cost]++;

        // re-assigning to originl array
        int ind = 0;
        for (int i = 0; i < freq.length; i++) {
            while (freq[i] > 0) {
                costs[ind++] = i;
                freq[i]--;
            }
        }

        int count = 0;
        for (int i : costs) {
            if (coins >= i) {
                count++;
                coins -= i;
            } else
                break;
        }
        return count;
    }
}
