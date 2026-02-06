# 771. Jewels and Stones
# in python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        jewels = set(jewels)
        # Time complexity : O(S * 1)
            # S --> stones, J --> jewels
        for i in stones:  # O(S)
            if i in jewels:  # O(1)
                c += 1
        return c

# in java
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> js = new HashSet<>();
        for (char j : jewels.toCharArray())
            js.add(j);

        int c = 0;
        for (char s : stones.toCharArray()) {
            if (js.contains(s))
                c++;
        }
        return c;
    }
}
