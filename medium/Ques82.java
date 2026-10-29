// 82. Remove Duplicates from Sorted List II
// in python
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)

        prev, curr = dummy, head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val

                while curr and curr.val == duplicate:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next
  

// in java
  class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        // dummy.next = head;

        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {
            if (curr.next != null && curr.val == curr.next.val) {
                int duplicate = curr.val;

                while (curr != null && curr.val == duplicate)
                    curr = curr.next;

                prev.next = curr;
            } else {
                prev = curr;
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}
