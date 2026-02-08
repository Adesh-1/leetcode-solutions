# 682. Baseball Game
# in python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)

# in java
class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        for (String op : operations) {
            if (op.equals("C"))
                stack.pop();
            else if (op.equals("D"))
                stack.push(2 * stack.peek());
            else if (op.equals("+")) {
                int last = stack.pop();
                int total = last + stack.peek();
                stack.push(last);
                stack.push(total);
            } else
                stack.push(Integer.parseInt(op));
        }
        int sum = 0;
        for (int i : stack)
            sum += i;

        return sum;
    }
}
