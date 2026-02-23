# 1461. Check If a String Contains All Binary Codes of Size K
# in python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()

        # Loop through all substrings of length k
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            seen.add(substring)

        # Total possible binary codes of length k
        return len(seen) == 2**k

        # For length k, total possible binary codes = 2^k

# in java
class Solution {
    public boolean hasAllCodes(String s, int k) {
        HashSet<String> seen = new HashSet<>();

        # // Loop through all substrings of length k
        for (int i = 0; i <= s.length() - k; i++) {
            String substring = s.substring(i, i + k);
            seen.add(substring);
        }

        # // Total possible binary codes of length k
        return seen.size() == (1 << k);      # // same as Math.pow(2, k)
    }
}
