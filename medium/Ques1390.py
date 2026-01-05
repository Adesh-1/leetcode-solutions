# 1390. Four Divisors
# in python 
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            divisors = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                ans += sum(divisors)
        return ans

# in java
class Solution {
    public int sumFourDivisors(int[] nums) {
        int ans = 0;
        for (int n : nums) {
            Set<Integer> divisors = new HashSet<>();
            for (int i = 1; i * i <= n; i++) {
                if (n % i == 0) {
                    divisors.add(i);
                    divisors.add(n / i);
                }
                if (divisors.size() > 4)
                    break;
            }
            if (divisors.size() == 4) {
                for (int s : divisors)
                    ans += s;
            }
        }
        return ans;
    }
}
