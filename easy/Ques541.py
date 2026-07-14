# 541. Reverse String II
# in python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l=list(s)
        for i in range(0,len(s),2*k):
            l[i:i+k]=reversed(l[i:i+k])
        return ''.join(l)

# in java
class Solution {
    public String reverseStr(String s, int k) {
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i += (2 * k)) {
            int st = i;
            int en = Math.min(i + k - 1, chars.length - 1);
            while (st < en) {
                char temp = chars[st];
                chars[st] = chars[en];
                chars[en] = temp;
                st++;
                en--;
            }
        }
        return new String(chars);
    }
}
