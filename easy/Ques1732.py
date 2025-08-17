# 1732. Find the Highest Altitude
# in py
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l,n = [],0
        l.append(0)
        for i in gain:
            n += i
            l.append(n)
        return max(l)

  # in java
  class Solution {
    public int largestAltitude(int[] gain) {
        int a = 0;
        int[] l = new int[gain.length + 1];
        l[0] = 0; # // l[a] = 0 bcz of a = 0 in first
        for(int i = 0; i < gain.length; i++)
            l[i+1] = l[i] + gain[i];
        
        for(int j : l){
            if(a < j) a = j;
        }
        return a;
    }
}
