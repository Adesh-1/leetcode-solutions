// 24. Swap Nodes in Pairs
// in java
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = first.next;

            // swap
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // move prev
            prev = first;
        }
        return dummy.next;
    }
}

// in python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap
            first.next = second.next
            second.next = first
            prev.next = second

            # move prev
            prev = first
        return dummy.next
