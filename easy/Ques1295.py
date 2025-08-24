# 1295. Find Numbers with Even Number of Digits
# in py
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                even_digit += 1
        return even_digit

# in java
      # with simple way
class Solution {
    public int findNumbers(int[] nums) {
        int countDigit = 0;
        for(int i : nums){
            int c = 0;
            while(i!=0){
                i/=10;
                c++;
            }
            if(c%2==0)
                countDigit++;
        }
        return countDigit;
    }
}

    # with converting int to string
'''
class Solution {
    public int findNumbers(int[] nums) {
        int countDigit = 0;
        for (int i : nums) {
            # String s = Integer.toString(i);
            if (Integer.toString(i).length() % 2 == 0)
                countDigit++;
        }
        return countDigit;
    }
}
'''
# for more info in java convention on int --> String follow below link
# https://chatgpt.com/share/68ab27d7-44b4-8001-9540-7b9b70100373
