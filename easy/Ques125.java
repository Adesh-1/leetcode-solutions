// 125. Valid Palindrome
// in java
class Solution {
    public boolean isPalindrome(String s) {
        // Remove all non-alphanumeric characters (spaces, punctuation, etc.) and convert to lowercase
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Check palindrome using StringBuilder reverse
        String reversed = new StringBuilder(s).reverse().toString();
        return s.equals(reversed);
    }
}

// in pyhton
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        l1 = [i.lower() for i in l if i.isalnum()]
        return l1 == l1[::-1]
