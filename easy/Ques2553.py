# 2553. Separate the Digits in an Array
# in python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num > 9:
                for i in str(num):
                    res.append(int(i))
            else:
                res.append(num)

        return res

# in java
class Solution {
    public int[] separateDigits(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for (int num : nums) {
            if (num > 9) {
                String s = String.valueOf(num);  # // can use Integer.toString(num)
                for (char ch : s.toCharArray())
                    res.add(ch - '0');
            } else
                res.add(num);
        }

        int[] ans = new int[res.size()];
        for (int i = 0; i < res.size(); i++)
            ans[i] = res.get(i);
        return ans;
    }
}
