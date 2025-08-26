# 442. Find All Duplicates in an Array
# in py
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l, d = [], Counter(nums)
        # d = Counter(nums)
        for k, v in d.items():
            if v > 1:
                l.append(k)
        return l

# in java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> l = new ArrayList<>(); 
            # in this i don't use set in place of list bcz in question specify that 
                # the element 'return an array of all the integers that appears twice.' 
        Set<Integer> s = new HashSet<>();
        for (int i : nums) {
            if (s.contains(i))
                l.add(i);
            else
                s.add(i);
        }
        return l;
    }
}
