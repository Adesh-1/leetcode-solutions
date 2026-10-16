// 92. Reverse Linked List II
// in java
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;
        for (int i = 1; i < left; i++)
            prev = prev.next;

        ListNode curr = prev.next;

        for (int i = 0; i < right - left; i++) {
            ListNode next = curr.next;
            curr.next = next.next;
            next.next = prev.next;
            prev.next = next;
        }
        return dummy.next;
    }
}

// in python
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        for i in range(1, left):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next

        return dummy.next
