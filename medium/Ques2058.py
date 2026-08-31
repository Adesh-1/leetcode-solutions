# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# in python
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = last = -1
        minDist = float("inf")

        while curr.next:
            next_node = curr.next
            pos += 1

            if (curr.val > prev.val and curr.val > next_node.val) or \
                (curr.val < prev.val and curr.val < next_node.val):

                if first == -1:
                    first = pos  # 'first' stores the first critical point.
                else:
                    minDist = min(minDist, pos - last)

                last = pos  # 'last' stores the most recent critical point.

            prev = curr
            curr = next_node

        if first == -1 or first == last:
            return [-1, -1]

        return [minDist, last - first]

# in java
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ListNode prev = head;
        ListNode curr = head.next;
        int pos = 1;

        int first = -1;
        int last = -1;
        int minDist = Integer.MAX_VALUE;

        while (curr.next != null) {
            ListNode nextNode = curr.next;
            pos++;

            if ((curr.val > prev.val && curr.val > nextNode.val) ||
                    (curr.val < prev.val && curr.val < nextNode.val)) {

                if (first == -1)
                    first = pos;
                else
                    minDist = Math.min(minDist, pos - last);

                last = pos;
            }

            prev = curr;
            curr = nextNode;
        }

        if (first == -1 || first == last)
            return new int[] { -1, -1 };

        return new int[] { minDist, last - first };
    }
}
