# 374. Guess Number Higher or Lower
# in py
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:  # or we can use elif like this --> 'elif guess(mid) == -1'
                right = mid - 1
        return -1

  # in java
  public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1, high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2; #// safe from overflow
            int res = guess(mid);
            if (res == 0) {
                return mid; #// found it
            } else if (res == 1) {
                low = mid + 1; #// pick is higher
            } else {
                high = mid - 1; #// pick is lower
            }
        }
        return -1; #// shouldn't happen
    }
}
