# 3718. Smallest Missing Multiple of K
# in python
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        i = 1
        while True:
            mul = k * i
            if mul not in s:
                return mul
            i += 1

# in java
class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums)
            set.add(num);

        for (int i = 1; ; i++) {
            if (!set.contains(k * i))
                return k * i;
        }
    }
}
