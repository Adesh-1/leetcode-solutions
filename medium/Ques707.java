// 707. Design Linked List
// in java
class MyLinkedList {
    
    private class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
            this.next = null;
        }
    }

    private Node head;
    private Node tail;
    private int size;

    public MyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    public int get(int index) {
        if (index >= size) // it also checks the 'head == null' bcz size=0
            return -1;

        Node temp = head;

        while (index != 0) {
            temp = temp.next;
            index--;
        }

        return temp.val;
    }

    public void addAtHead(int val) {
        Node newNode = new Node(val);
        size++;

        if (head == null) {
            head = tail = newNode;
            return;
        }

        newNode.next = head;
        head = newNode;
    }

    public void addAtTail(int val) {
        Node newNode = new Node(val);
        size++;

        if (head == null) {
            head = tail = newNode;
            return;
        }

        tail.next = newNode;
        tail = newNode;
    }

    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }

        if (index == size) {
            addAtTail(val);
            return;
        }

        if (index > size)
            return;

        Node newNode = new Node(val);
        size++;
        int i = 0;
        Node temp = head;

        while (i < index - 1) {
            temp = temp.next;
            i++;
        }

        newNode.next = temp.next;
        temp.next = newNode;
    }

    public void deleteAtIndex(int index) {
        if (head == null) {
            tail = null;
            return;
        }

        if (index >= size)
            return;

        size--;

        if (index == 0) {
            head = head.next;
            if (head == null)
                tail = null;
            return;
        }

        int i = 0;
        Node temp = head;

        while (i < index - 1) {
            temp = temp.next;
            i++;
        }

        if (temp.next.next == null) {
            tail = temp;
            temp.next = null;
            return;
        }

        temp.next = temp.next.next;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
