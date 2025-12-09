// 506. Relative Ranks
// in java
class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;

        // store [score, index]
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = score[i];
            arr[i][1] = i;
        }

        // sort by score descending
        Arrays.sort(arr, (a, b) -> b[0] - a[0]);

        String[] res = new String[n];

        for (int i = 0; i < n; i++) {
            int idx = arr[i][1];

            if (i == 0) res[idx] = "Gold Medal";
            else if (i == 1) res[idx] = "Silver Medal";
            else if (i == 2) res[idx] = "Bronze Medal";
            else res[idx] = String.valueOf(i + 1);
        }

        return res;
    }
}


// in python
class Solution:
    def findRelativeRanks(self, score):
        arr = [(s, i) for i, s in enumerate(score)]
        arr.sort(reverse=True)  # sort by score descending

        res = [""] * len(score)

        for rank, (s, idx) in enumerate(arr):
            if rank == 0:
                res[idx] = "Gold Medal"
            elif rank == 1:
                res[idx] = "Silver Medal"
            elif rank == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank + 1)

        return res
