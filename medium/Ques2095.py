# 2095. Delete the Middle Node of a Linked List
# in python
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        prev = None
        slow = fast = head

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head

# in java
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        // If there is only one node
        if (head.next == null)
            return null;

        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // Delete the middle node
        prev.next = slow.next;
        return head;
    }
}
