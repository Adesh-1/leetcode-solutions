# 950. Reveal Cards In Increasing Order
# in python
class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        queue = []

        for i in range(len(deck)):
            queue.append(i)

        ans = [0] * len(deck)
        
        for num in deck:
            ind = queue.pop(0)
            ans[ind] = num

            if queue:
                queue.append(queue.pop(0))

        return ans

# in java
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < deck.length; i++)
            q.offer(i);

        int[] ans = new int[deck.length];

        for (int card : deck) {
            int ind = q.poll();
            ans[ind] = card;

            if (!q.isEmpty())
                q.offer(q.poll());
        }
        return ans;
    }
}
