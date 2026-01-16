# 155. Min Stack
# in python
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:        # if len(self.minStack) == 0 
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# in java
class MinStack {
    
    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty())
            minStack.push(val);
        else
            minStack.push(Math.min(val, minStack.peek()));
    }

    public void pop() {
        stack.pop();
        minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
