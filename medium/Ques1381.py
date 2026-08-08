# 1381. Design a Stack With Increment Operation
# in python
class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) != self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        n = min(k, len(self.stack))
        for i in range(n):
            self.stack[i] += val

# in java
class CustomStack {
    private int size;
    private List<Integer> stack;

    public CustomStack(int maxSize) {
        size = maxSize;
        stack = new ArrayList<>();
    }

    public void push(int x) {
        if (stack.size() != size)
            stack.add(x);
    }

    public int pop() {
        if (stack.isEmpty())
            return -1;
        return stack.remove(stack.size() - 1);
    }

    public void increment(int k, int val) {
        int min = Math.min(k, stack.size());
        for (int i = 0; i < min; i++)
            stack.set(i, stack.get(i) + val);
    }
}
