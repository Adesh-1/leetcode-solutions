# 1665. Minimum Initial Energy to Finish Tasks
# in python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        energy = 0
        current = 0

        for actual, minimum in tasks:
            energy = max(energy, current + minimum)
            current += actual

        return energy

# in java
class Solution {
    public int minimumEffort(int[][] tasks) {

        Arrays.sort(tasks, (a, b) -> {
            return (b[1] - b[0]) - (a[1] - a[0]);
        });

        int energy = 0;
        int current = 0;

        for (int[] task : tasks) {

            int actual = task[0];
            int minimum = task[1];

            energy = Math.max(energy, current + minimum);

            current += actual;
        }

        return energy;
    }
}
