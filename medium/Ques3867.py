# 3867. Sum of GCD of Formed Pairs
# in python
from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pre, m = [], 0
        for i in nums:
            m = max(m, i)
            pre.append(gcd(i, m))
        pre.sort()

        l, r = 0, len(pre) - 1
        ans = 0
        while l < r:
            ans += gcd(pre[l], pre[r])
            l += 1
            r -= 1
        return ans

# in java
class Solution {
    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public long gcdSum(int[] nums) {
        int[] pre = new int[nums.length];
        int m = 0;
        for (int i = 0; i < nums.length; i++) {
            m = Math.max(m, nums[i]);
            pre[i] = gcd(nums[i], m);
        }
        Arrays.sort(pre);

        int l = 0, r = pre.length - 1;
        long sum = 0;
        while (l < r) {
            sum += gcd(pre[l], pre[r]);
            l++;
            r--;
        }
        return sum;
    }
}
