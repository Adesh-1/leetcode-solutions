# 414. Third Maximum Number
# in python
# 1st method
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        l.sort(reverse=True)
        if len(l) < 3:
            return max(l)
        return l[2]

# 2nd method
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        l.sort()
        l.reverse()
        if len(l) < 3:
            return max(l)
        return l[2]

# in java
class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int n : nums)
            set.add(n);

        List<Integer> list = new ArrayList<>(set);

        Collections.sort(list, Collections.reverseOrder()); // sort descending

        return list.size() >= 3 ? list.get(2) : list.get(0);
    }
}
