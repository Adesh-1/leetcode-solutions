# 229. Majority Element II
# in python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        d = Counter(nums)
        t = len(nums) // 3
        for k, v in d.items():
            if v > t:
                ans.append(k)
        return ans

# in java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        # // Count frequency of each element
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int t = nums.length / 3;

        # // Check elements with frequency > n/3
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > t) {
                ans.add(entry.getKey());
            }
        }

        return ans;
    }
}
