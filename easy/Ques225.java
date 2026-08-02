// 225. Implement Stack using Queues
// in java
class MyStack {

    private Queue<Integer> q1;
    private Queue<Integer> q2;

    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }

    public void push(int x) {
        if (!q1.isEmpty())
            q1.add(x);
        else
            q2.add(x);
    }

    public int pop() {
        if (empty())
            return -1;

        int top = -1;
        // case 1 where elements store in q1
        if (!q1.isEmpty()) {
            while (!q1.isEmpty()) {
                top = q1.remove();

                if (q1.isEmpty())
                    break;

                q2.add(top);
            }
        } else { // case 2 where elements store in q2
            while (!q2.isEmpty()) {
                top = q2.remove();

                if (q2.isEmpty())
                    break;

                q1.add(top);
            }
        }
        return top;
    }

    public int top() {
        if (empty())
            return -1;

        int top = -1;
        // case 1 where elements store in q1
        if (!q1.isEmpty()) {
            while (!q1.isEmpty()) {
                top = q1.remove();
                q2.add(top);
            }
        } else { // case 2 where elements store in q2
            while (!q2.isEmpty()) {
                top = q2.remove();
                q1.add(top);
            }
        }
        return top;
    }

    public boolean empty() {
        return q1.isEmpty() && q2.isEmpty();
    }
}

// in python
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1

        top = -1
        // # case 1
        if self.q1:
            while self.q1:
                top = self.q1.popleft()

                if not self.q1:
                    break

                self.q2.append(top)
        else:  // # case 2
            while self.q2:
                top = self.q2.popleft()

                if not self.q2:
                    break

                self.q1.append(top)

        return top

    def top(self) -> int:
        if self.empty():
            return -1

        top = -1
        // # case 1
        if self.q1:
            while self.q1:
                top = self.q1.popleft()
                self.q2.append(top)
        else:  // # case 2
            while self.q2:
                top = self.q2.popleft()
                self.q1.append(top)

        return top

    def empty(self) -> bool:
        return not self.q1 and not self.q2
