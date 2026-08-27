# 2. Add Two Numbers
# in java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int n1 = (l1 != null) ? l1.val : 0;
            int n2 = (l2 != null) ? l2.val : 0;

            int total = n1 + n2 + carry;
            carry = total / 10;

            ListNode nextNode = new ListNode(total % 10);
            curr.next = nextNode;
            curr = curr.next;

            if (l1 != null)
                l1 = l1.next;

            if (l2 != null)
                l2 = l2.next;
        }
        return dummy.next;
    }
}

# in python
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        c = 0
        r = n = ListNode(0)
        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            c, val = divmod(c, 10)    # divmod(a, b) returns: (a // b, a % b)
            n.next = n = ListNode(val)
        return r.next
