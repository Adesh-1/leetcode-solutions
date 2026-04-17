# 1528. Shuffle String
# in python
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [''] * len(s)
        for i, ind in enumerate(indices):
            l[ind] = s[i]
        return ''.join(l)

# in java
class Solution {
    public String restoreString(String s, int[] indices) {
        char[] res = new char[s.length()];
        for (int i = 0; i < indices.length; i++)
            res[indices[i]] = s.charAt(i);
        return new String(res);
    }
}
