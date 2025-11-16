// 150. Evaluate Reverse Polish Notation
// in java
class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> st = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+":
                    st.push(st.pop() + st.pop());
                    break;
                case "-": {
                    int b = st.pop();
                    int a = st.pop();
                    st.push(a - b);
                    break;
                }
                case "*":
                    st.push(st.pop() * st.pop());
                    break;
                case "/": {
                    int b = st.pop();
                    int a = st.pop();
                    st.push(a / b); // Java int division truncates toward zero
                    break;
                }
                default:
                    st.push(Integer.parseInt(t));
            }
        }
        return st.peek();
    }
}

// in python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[-1]
