// 540. Single Element in a Sorted Array
// in java
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n = 0;
        for(int num : nums)
            n ^= num;
        return n;
    }
}

// in python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s ^= i
        return s
  /*
➡️ s = 0   (start from 0)
s ^ 1 = 1
1 ^ 1 = 0   (1’s cancel out)
0 ^ 2 = 2   (single stays so far)
2 ^ 3 = 1
1 ^ 3 = 2   (3’s cancel out, 2 stays)
2 ^ 4 = 6
6 ^ 4 = 2   (4’s cancel out, 2 stays)
2 ^ 8 = 10
10 ^ 8 = 2  (8’s cancel out, 2 stays)

Final s = 2 ✅

➡️for ex.
s = 2 ^ 3
How do we evaluate 2 ^ 3?

Write them in binary:

2 = 10 (in binary)

3 = 11 (in binary)

XOR means “different bits = 1, same bits = 0”:

  10   (2)
^ 11   (3)
 ----
  01   (1)


➡️So, 2 ^ 3 = 1.
Now s = 1.
Step 2
s = 1 ^ 3
Binary:
1 = 01
3 = 11
  01   (1)
^ 11   (3)
 ----
  10   (2)

So, 1 ^ 3 = 2.
Now s = 2 again ✅
  */

  // for more info https://chatgpt.com/share/68a4af9a-ed74-8001-bf51-4a400e4c41fa
