# 1018. Binary Prefix Divisible By 5
# in python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0  # current prefix value modulo 5
        for bit in nums:
            cur = ((cur << 1) + bit) % 5   # same as cur = (cur * 2 + bit) % 5
            res.append(cur == 0)
        return res

# in java
class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> res = new ArrayList<>();
        int cur = 0;
        for (int bit : nums) {
            cur = ((cur * 2) + bit) % 5;
            res.add(cur == 0);
        }
        return res;
    }
}
