# 443. String Compression
# in python
class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)
        while read < n:
            ch = chars[read]
            count = 0
            while read < n and chars[read] == ch:
                read += 1
                count += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write

# in java
class Solution {
    public int compress(char[] chars) {
        int read = 0, write = 0;
        int n = chars.length;
        while (read < n) {
            char ch = chars[read];
            int count = 0;
            while (read < n && chars[read] == ch) {
                read++;
                count++;
            }
            chars[write] = ch;
            write++;
            if (count > 1) {
                for (char digit : String.valueOf(count).toCharArray()) {
                    chars[write] = digit;
                    write++;
                }
            }
        }
        return write;
    }
}
