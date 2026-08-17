# 678. Valid Parenthesis String
# in python
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
      
        for ch in s:
            if ch == "(":
                low += 1
                high += 1
            elif ch == ")":
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1
              
            if high < 0:
                return False
              
            low = max(low, 0)
          
        return low == 0

# in java
class Solution {
    public boolean checkValidString(String s) {
        int low = 0, high = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                low++;
                high++;
            } else if (ch == ')') {
                low--;
                high--;
            } else { // ch == '*'
                low--;
                high++;
            }

            if (high < 0)
                return false;

            low = Math.max(low, 0);
        }
        return low == 0;
    }
}
