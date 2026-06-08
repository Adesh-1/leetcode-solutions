# 2161. Partition Array According to Given Pivot
# in python
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)

        return less + equal + greater

# in java
class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> list = new ArrayList<>();
        for (int i : nums)
            if (i < pivot)
                list.add(i);

        for (int i : nums)
            if (i == pivot)
                list.add(i);

        for (int i : nums)
            if (i > pivot)
                list.add(i);

        int[] ans = new int[list.size()];
        for (int i = 0; i < list.size(); i++)
            ans[i] = list.get(i);

        return ans;
    }
}
