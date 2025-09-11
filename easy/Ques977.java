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
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_list = [i**2 for i in nums]
        sq_list.sort()
        return sq_list
