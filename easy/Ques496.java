// 496. Next Greater Element I
// in java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        Stack<Integer> stack = new Stack<>();
        Map<Integer, Integer> map = new HashMap<>();

        // Find next greater for each element in nums2
        for (int num : nums2) {
            // If current number is greater than stack top,
            // it is the next greater element
            while (!stack.isEmpty() && num > stack.peek()) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }

        // Remaining elements have no greater element
        while (!stack.isEmpty()) {
            map.put(stack.pop(), -1);
        }

        // Build answer for nums1
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            ans[i] = map.get(nums1[i]);
        }

        return ans;
    }
}

// in python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mp = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)

        while stack:
            mp[stack.pop()] = -1

        return [mp[num] for num in nums1]

// for more info follow below link
// https://chatgpt.com/share/698cc487-82d4-8001-8634-341f30ae7d6d
