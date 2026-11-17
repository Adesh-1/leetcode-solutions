# 2243. Calculate Digit Sum of a String
# in python
class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            ns = []    # ns = new_string

            for i in range(0, len(s), k):
                st = s[i : i + k]
                ns.append(str(sum(map(int, st))))    # cal sum then convert to str

            s = "".join(ns)

        return s

# in java
class Solution {
    public String digitSum(String s, int k) {

        while (s.length() > k) {

            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < s.length(); i += k) {
                int sum = 0;
                
                for (int j = i; j < Math.min(i + k, s.length()); j++)
                    sum += s.charAt(j) - '0';

                sb.append(sum);
            }

            s = sb.toString();
        }

        return s;
    }
}
