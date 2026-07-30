# 3014. Minimum Number of Pushes to Type Word I
# in python
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(i // 8 + 1 for i in range(len(word)))

# in java
class Solution {
    public int minimumPushes(String word) {
        int ans = 0;
        for (int i = 0; i < word.length(); i++)
            ans += i / 8 + 1;
        return ans;
    }
}
