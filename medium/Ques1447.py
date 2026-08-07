# 1447. Simplified Fractions
# in python
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for denominator in range(2, n + 1):
            for numenator in range(1, denominator):
                if gcd(numenator, denominator) == 1:
                    ans.append(f"{numenator}/{denominator}")
        return ans

# in java
class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> ans = new ArrayList<>();

        for (int den = 2; den <= n; den++) {
            for (int num = 1; num < den; num++) {
                if (gcd(num, den) == 1)
                    ans.add(num + "/" + den);
            }
        }

        return ans;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

}
