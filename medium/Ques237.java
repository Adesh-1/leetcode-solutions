// 237. Delete Node in a Linked List
// in java
class Solution {
    public void deleteNode(ListNode node) {
        node.val=node.next.val;
        node.next=node.next.next;
    }
}

// exactly same for Python
