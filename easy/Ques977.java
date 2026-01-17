// 977. Squares of a Sorted Array
// in java
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] sqArr = new int[nums.length];
        for (int i = 0; i < sqArr.length; i++)
            sqArr[i] = (int) Math.pow(nums[i], 2); // using pow(a, b) & typecaste into 'int' because pow() returns 'double' by default
        Arrays.sort(sqArr);
        return sqArr;
    }
}

// in pyhton
    // 1st method 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_list = [i**2 for i in nums]
        sq_list.sort()
        return sq_list

    // 2nd method  O(n) time complexity
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sq = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                val = nums[l]
                l += 1
            else:
                val = nums[r]
                r -= 1
            sq[i] = val**2
        return sq
