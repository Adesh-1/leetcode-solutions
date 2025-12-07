# 3769. Sort Integers by Binary Reflection
# in python
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflected(x: int) -> int:
            # binary without '0b', reversed, convert back to int
            return int(bin(x)[2:][::-1], 2)
        
        # sort by (reflected value, original value) and return the reordered list
        return sorted(nums, key=lambda x: (reflected(x), x))

# for understand the code follow the below link -->
# https://chatgpt.com/share/6935b415-97e0-8001-91d3-2033a08b4b4e

# in java
import java.util.*;

class Solution {
    public int[] sortByReflection(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int x : nums) list.add(x);

        # // Sort using custom comparator
        Collections.sort(list, (a, b) -> {
            int ra = reflected(a);
            int rb = reflected(b);

            if (ra != rb) 
                return Integer.compare(ra, rb);  # // sort by reflected value first
            
            return Integer.compare(a, b);         # // tie → sort by original value
        });

        # // Convert back to int[]
        for (int i = 0; i < nums.length; i++) {
            nums[i] = list.get(i);
        }

        return nums;
    }

    private int reflected(int x) {
        String bin = Integer.toBinaryString(x);   
        String rev = new StringBuilder(bin).reverse().toString();  
        return Integer.parseInt(rev, 2);          
    }
}
