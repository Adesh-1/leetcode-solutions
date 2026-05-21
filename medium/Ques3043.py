# 3043. Find the Length of the Longest Common Prefix
# in python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # store all prefixes from arr1
        for num in arr1:
            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0

        # check prefixes of arr2
        for num in arr2:
            s = str(num)

            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans

# in java
class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        HashSet<String> prefixes = new HashSet<>();

        # // store all prefixes from arr1
        for (int num : arr1) {
            String s = String.valueOf(num);

            for (int i = 1; i <= s.length(); i++) {
                prefixes.add(s.substring(0, i));
            }
        }

        int ans = 0;

        # // check prefixes of arr2
        for (int num : arr2) {
            String s = String.valueOf(num);

            for (int i = 1; i <= s.length(); i++) {
                if (prefixes.contains(s.substring(0, i))) {
                    ans = Math.max(ans, i);
                }
            }
        }

        return ans;
    }
}
