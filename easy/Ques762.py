# 762. Prime Number of Set Bits in Binary Representation
# in python
    # 1st method
class Solution:
    def isPrime(self, n):
        if n <= 1:
            return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1

    def countPrimeSetBits(self, left: int, right: int) -> int:
        c = 0
        for i in range(left, right + 1):
            b = f"{i:b}".count("1")
            c += self.isPrime(b)
        return c

      # 2nd method
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        c = 0
        for i in range(left, right + 1):
            if bin(i).count("1") in primes:
                c += 1
        return c

      # 3rd mehtod
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(i.bit_count() in primes for i in range(left, right + 1))


# in java
class Solution {
    public int countPrimeSetBits(int left, int right) {
        Set<Integer> primes = new HashSet<>(
                Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19));

        int count = 0;

        for (int i = left; i <= right; i++) {
            if (primes.contains(Integer.bitCount(i))) {
                count++;
            }
        }

        return count;
    }
}
