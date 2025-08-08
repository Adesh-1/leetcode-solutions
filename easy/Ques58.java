// 58. Length of Last Word

// In JAVA
class Solution {
    public int lengthOfLastWord(String s) {
        int l = 0;
        boolean b = false;
        for(int i = s.length()-1; i >= 0; i--){
            char c = s.charAt(i);
            if(c != ' '){
                b = true;
                l++;
            }
            else{
                if(b)
                    break;
            }
        }
        return l;
    }
}

// In Python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1])
