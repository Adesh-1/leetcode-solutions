# 2840. Check if Strings Can be Made Equal With Operations II
# in python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2])==Counter(s2[::2]) and \
                Counter(s1[1::2])==Counter(s2[1::2])

# in java
class Solution {
    public boolean checkStrings(String s1, String s2) {
        int[] even1 = new int[26];
        int[] odd1 = new int[26];
        int[] even2 = new int[26];
        int[] odd2 = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);

            if (i % 2 == 0) {
                even1[c1 - 'a']++;
                even2[c2 - 'a']++;
            } else {
                odd1[c1 - 'a']++;
                odd2[c2 - 'a']++;
            }
        }

        # // Compare arrays
        for (int i = 0; i < 26; i++) {
            if (even1[i] != even2[i] || odd1[i] != odd2[i]) {
                return false;
            }
        }

        return true;
    }
}
