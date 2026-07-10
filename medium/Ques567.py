# 567. Permutation in String
# in python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26

        # Count characters of s1 and first window of s2
        for i in range(len(s1)):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1

        if cnt1 == cnt2:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):
            cnt2[ord(s2[i]) - ord('a')] += 1                  # Add new character
            cnt2[ord(s2[i - len(s1)]) - ord('a')] -= 1        # Remove old character

            if cnt1 == cnt2:
                return True

        return False

# in java
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];

        // Count frequencies of s1 and first window of s2
        for (int i = 0; i < s1.length(); i++) {
            cnt1[s1.charAt(i) - 'a']++;
            cnt2[s2.charAt(i) - 'a']++;
        }

        // Check first window
        if (isEqual(cnt1, cnt2)) {
            return true;
        }

        // Slide the window
        for (int i = s1.length(); i < s2.length(); i++) {
            cnt2[s2.charAt(i) - 'a']++;                    // Add new character
            cnt2[s2.charAt(i - s1.length()) - 'a']--;      // Remove old character

            if (isEqual(cnt1, cnt2)) {
                return true;
            }
        }

        return false;
    }

    private boolean isEqual(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }
}
