# 1980. Find Unique Binary String
# in python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            res.append('1' if nums[i][i]=='0' else '0')
        return "".join(res)

# in java
class Solution {
    public String findDifferentBinaryString(String[] nums) {
        char[] res = new char[nums.length];

        for (int i = 0; i < nums.length; i++) {
            res[i] = nums[i].charAt(i) == '0' ? '1' : '0';
        }

        return new String(res);
    }
}
