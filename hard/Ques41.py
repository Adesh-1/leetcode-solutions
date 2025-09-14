# 41. First Missing Positive
# in pyhton
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)  # ✅ convert list to set for O(1) lookup
            # bcz Membership check = O(n) for list, O(1) for set
        for i in range(1, len(nums) + 2):  # we check up to n+1 
                # if nums = [1] then output is 2 so that's why use len + 2
            if i not in nums_set:  # ✅ faster check
                return i

# in java
import java.util.*;

class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            numsSet.add(num);  // ✅ convert array to set
        }

        for (int i = 1; i <= nums.length + 1; i++) {  // check up to n+1
            if (!numsSet.contains(i)) {              // ✅ O(1) lookup
                return i;
            }
        }

        return -1; // should never reach here
    }
}
