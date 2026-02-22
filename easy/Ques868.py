# 868. Binary Gap
# in python
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = f"{n:b}"  # convert to binary and remove '0b'

        last_index = -1
        max_distance = 0

        for i in range(len(binary)):
            if binary[i] == "1":
                if last_index != -1:
                    distance = i - last_index
                    max_distance = max(max_distance, distance)
                last_index = i

        return max_distance

# in java
class Solution {
    public int binaryGap(int n) {
        String b = Integer.toBinaryString(n);
        int li = -1;
        int md = 0;

        for (int i = 0; i < b.length(); i++) {
            if (b.charAt(i) == '1') {
                if (li != -1) {
                    int d = i - li;
                    md = Math.max(md, d);
                }
                li = i;
            }
        }
        return md;
    }
}
