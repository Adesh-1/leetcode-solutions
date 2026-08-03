# 946. Validate Stack Sequences
# in python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack

# in java
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;

        for (int num : pushed) {
            stack.push(num);

            while (!stack.isEmpty() && stack.peek() == popped[i]) {
                stack.pop();
                i++;
            }
        }
        
        return stack.isEmpty();
    }
}
