// 2454. Next Greater Element IV
// in java
class Solution {
    public int[] secondGreaterElement(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, -1);

        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();
        List<Integer> temp = new ArrayList<>();

        for (int i = 0; i < n; i++) {

            // Found second greater
            while (!s2.isEmpty() && nums[s2.peek()] < nums[i]) {
                ans[s2.pop()] = nums[i];
            }

            // Move indices that found first greater
            while (!s1.isEmpty() && nums[s1.peek()] < nums[i]) {
                temp.add(s1.pop());
            }

            // Preserve order while moving to s2
            for (int j = temp.size() - 1; j >= 0; j--) {
                s2.push(temp.get(j));
            }
            temp.clear();

            s1.push(i);
        }

        return ans;
    }
}
