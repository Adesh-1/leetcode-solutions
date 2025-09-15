// 350. Intersection of Two Arrays II
// in java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;

        // frequency array to count elements in nums1
        int[] arr = new int[1001];   // since constraints: nums[i] <= 1000
        for (int i : nums1) {
            arr[i]++;   // count how many times each number appears in nums1
        }

        // temporary array for storing intersection
        int[] a = new int[Math.min(n, m)];
        int x = 0;

        // check nums2 against frequency array
        for (int i : nums2) {
            if (arr[i] != 0) {   // if number exists in nums1
                a[x] = i;        // add it to result
                x++;
                arr[i]--;        // decrease frequency (use it once)
            }
        }

        // shrink to exact size
        int[] ans = new int[x];
        for (int i = 0; i < x; i++) {
            ans[i] = a[i];
        }

        return ans;
    }
}

// in pyhton
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = s1.intersection(s2)
        res = []
        for i in s3:
            c = min(nums1.count(i), nums2.count(i))
            while c >= 1:
                res.append(i)
                c -= 1
        return res
