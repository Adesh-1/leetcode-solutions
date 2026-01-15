# 451. Sort Characters By Frequency
# in python
    # 1st method
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join([k * v for k, v in c.most_common()])

    # 2nd method
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sd = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
        return "".join([k * v for k, v in sd.items()])

# in java
class Solution {
    public String frequencySort(String s) {
        
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char ch : s.toCharArray()) {
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Character, Integer>> maxHeap =
            new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());

        maxHeap.addAll(freqMap.entrySet());

        StringBuilder sb = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            Map.Entry<Character, Integer> entry = maxHeap.poll();
            char ch = entry.getKey();
            int freq = entry.getValue();
            for (int i = 0; i < freq; i++) {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}
