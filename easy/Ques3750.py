# 3750. Minimum Number of Flips to Reverse Binary String
# in python
class Solution:
    def minimumFlips(self, n: int) -> int:
        # Convert the integer to its binary representation as a string (without '0b')
        b = f"{n:b}"

        # Convert the binary string to a list of characters for easy indexing
        lb = list(b)

        # Create a reversed copy of the list (lb[::-1] does NOT modify original)
        lrb = list(reversed(lb))  # can write lb[::-1]
 
        # If the binary string is already a palindrome, no flips are needed
        if lb == lrb:
            return 0

        # Count the number of mismatched positions
        c = 0
        for i in range(len(lb)):
            # Compare original and reversed bits at each index
            # If they differ, one flip is required for this position
            if lb[i] != lrb[i]:
                c += 1

        # Return total flips required
        return c

# in java
class Solution {
    public int minimumFlips(int n) {
        String b = Integer.toBinaryString(n);
        int len = b.length();
        int flips = 0;

        for (int i = 0; i < len / 2; i++) {
            if (b.charAt(i) != b.charAt(len - 1 - i)) {
                flips++;
            }
        }

        return flips * 2;   #// bcz 2 filps/mismatch
    }
}
