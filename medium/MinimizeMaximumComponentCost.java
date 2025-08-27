/* 
Ques 3612
Minimize Maximum Component Cost

You are given an undirected connected graph with n nodes labeled from 0 to n - 1 and a 2D integer array edges where edges[i] = [ui, vi, wi] denotes an undirected edge between node ui and node vi with weight wi, and an integer k.

You are allowed to remove any number of edges from the graph such that the resulting graph has at most k connected components.

The cost of a component is defined as the maximum edge weight in that component. If a component has no edges, its cost is 0.

Return the minimum possible value of the maximum cost among all components after such removals.
*/

 

Example 1:

Input: n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2

Output: 4

Explanation:



Remove the edge between nodes 3 and 4 (weight 6).
The resulting components have costs of 0 and 4, so the overall maximum cost is 4.
Example 2:

Input: n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1

Output: 5


import java.util.*;

class Solution {
    public int minCost(int n, int[][] edges, int k) {
        Arrays.sort(edges, Comparator.comparingInt(a -> a[2]));

        UnionFind uf = new UnionFind(n);
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int[] edge : edges) {
            if (uf.union(edge[0], edge[1])) {
                maxHeap.offer(edge[2]);
                if (maxHeap.size() == n - 1) break; // MST done
            }
        }

        // Remove (k - 1) heaviest edges
        for (int i = 0; i < k - 1 && !maxHeap.isEmpty(); i++) {
            maxHeap.poll();
        }

        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }

    class UnionFind {
        int[] parent, rank;

        UnionFind(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x)
                parent[x] = find(parent[x]);
            return parent[x];
        }

        boolean union(int x, int y) {
            int rootX = find(x), rootY = find(y);
            if (rootX == rootY) return false;
            if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;
            else if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;
            else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }
    }
}
