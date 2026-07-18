// 234. Palindrome Linked List
// in java
class Solution {
    private ListNode findMid(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public boolean isPalindrome(ListNode head) {
        // corner case
        if (head == null || head.next == null)
            return true;

        // 1st --> find mid
        ListNode mid = findMid(head);

        // 2nd --> reverse from mid
        ListNode prev = null;
        ListNode curr = mid;
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        // 3rd --> check left and right LinkedList
        ListNode right = prev;
        ListNode left = head;
        while (right != null) {
            if (left.val != right.val)
                return false;
            left = left.next;
            right = right.next;
        }
        return true;
    }
}
  
// in python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        // # corner case
        if not head or not head.next:
            return True

        def findMid(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        // # cal reverse & find mid
        prev = None
        curr = findMid(head)
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        // # check left & right
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

