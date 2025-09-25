# 2413. Smallest Even Multiple
# in python
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2

# in java
class Solution {
    public int smallestEvenMultiple(int n) {
        if (n % 2 == 0)
            return n;
        else
            return n * 2;
    }
}

# for explanation of MULTIPLE follow below link
# https://chatgpt.com/share/68d57919-4e04-8001-ba7d-a7fd9a202fd3
# A multiple of a number means a number that is divisible by that number (without remainder).

# Example 1: Multiples of 5

# 5×1=5
# 5×2=10
# 5×4=20

# So multiples of 5 = 5, 10, 15, 20, …
# Each of these is divisible by 5.

# Example 2: Multiples of 2

# 2×1=2
# 2×2=4
# 2×3=6
# 2×4=8

# So multiples of 2 = 2, 4, 6, 8, …
# Each of these is divisible by 2.
