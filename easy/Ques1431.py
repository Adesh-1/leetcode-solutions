# 1431. Kids With the Greatest Number of Candies
# in python 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies)
        l = []
        for i in candies:
            a = i + extraCandies
            # if a >= n:
            #     l.append(True)
            # else:
            #     l.append(False)
            l.append(a >= n)
        return l

# in java
class Solution {
    private int findMax(int[] arr) {
        int no = 0;
        for (int i : arr)
            no = i > no ? i : no;
        return no;
    }

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> c = new ArrayList<>();
        int max = findMax(candies);
        for (int i : candies) {
            // int n = i + extraCandies;
            // if(n >= max) c.add(true); 
            // else{c.add(false);} 
                    // no matter to use {} or not use
            c.add(i + extraCandies >= max);
        }
        return c;
    }
}
