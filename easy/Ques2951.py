# 2951. Find the Peaks
# in python
  # 1st method
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peak = []
        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                peak.append(i)
        return peak

  # 2nd method
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain) - 1)
                if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]]

# in java
class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        List<Integer> peaks = new ArrayList<>();
        for (int i = 1; i < mountain.length - 1; i++) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                peaks.add(i);
            }
        }
        return peaks;
    }
}
