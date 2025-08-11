// 1470. Shuffle the Array
// in java
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] a = new int[n * 2];
        int ind = 0;
        for(int i = 0; i < n; i++){
            a[ind++] = nums[i];
            a[ind++] = nums[n + i];
        }
        return a;
    }
}

// in py
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[n+i])
        return l
