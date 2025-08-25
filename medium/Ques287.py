# 287. Find the Duplicate Number
# in py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d1 = Counter(nums)
        for k, v in d1.items():
            if v > 1:
                return k
        return -1

# in java
class Solution {
    public int findDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for(int i : nums){
            if(s.contains(i))
                return i;
            else
                s.add(i);
        }
        return -1;
    }
}
