// 349. Intersection of Two Arrays
// in pyhton
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & (set(nums2)))


// in java
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        // convert nums1 to set1
        Set<Integer> s1 = new HashSet<>();
        for (int i : nums1)
            s1.add(i);

        // convert nums2 to set2
        Set<Integer> s2 = new HashSet<>();
        for (int i : nums2)
            s2.add(i);

        s1.retainAll(s2); // Perform intersection (like Python's &)

        // Directly build int[] from set
        int[] res = new int[s1.size()];
        int idx = 0;
        for (int i : s1)
            res[idx++] = i;

        return res;
    }
}

