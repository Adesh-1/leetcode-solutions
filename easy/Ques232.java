// 232. Implement Queue using Stacks
// in java
class MyQueue {
    
    private Stack<Integer> s1;
    private Stack<Integer> s2;

    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }

    public void push(int x) {
        while (!s1.isEmpty())
            s2.push(s1.pop());

        s1.push(x);

        while (!s2.isEmpty())
            s1.push(s2.pop());
    }

    public int pop() {
        if (s1.empty())
            return -1;
        return s1.pop();
    }

    public int peek() {
        if (s1.empty())
            return -1;
        return s1.peek();
    }

    public boolean empty() {
        return s1.isEmpty();
    }
}

// in python
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if self.empty():
            return -1
        return self.s1.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
