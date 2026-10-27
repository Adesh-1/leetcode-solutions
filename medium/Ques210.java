// 210. Course Schedule II
// in java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // create graph
        List<List<Integer>> graph = new ArrayList<>();

        // initialize each vertex
        for (int i = 0; i < numCourses; i++)
            graph.add(new ArrayList<>());

        int[] indeg = new int[numCourses];

        // store connections in graph
        for (int[] p : prerequisites) {
            int course = p[0];
            int prerequisite = p[1];

            graph.get(prerequisite).add(course);

            indeg[course]++; // count in-degree for each vertex
        }

        Queue<Integer> q = new LinkedList<>();

        // add all 0 in-degree vertex in queue 
        for (int ver = 0; ver < indeg.length; ver++)
            if (indeg[ver] == 0)
                q.add(ver);

        int[] order = new int[numCourses];
        int ind = 0;

        // same logic of BFS
        while (!q.isEmpty()) {
            int curr = q.remove();
            order[ind++] = curr;

            for (int dest : graph.get(curr)) {
                indeg[dest]--;

                if (indeg[dest] == 0)
                    q.add(dest);
            }
        }

        // If some courses remain, a cycle exists
        if (ind != numCourses)
            return new int[0];

        return order;
    }
}

// in python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indeg[course] += 1

        q = deque()

        for ver in range(numCourses):
            if indeg[ver] == 0:
                q.append(ver)

        order = []

        while q:
            curr = q.popleft()
            order.append(curr)

            for dest in graph[curr]:
                indeg[dest] -= 1

                if indeg[dest] == 0:
                    q.append(dest)

        if len(order) != numCourses:
            return []

        return order
