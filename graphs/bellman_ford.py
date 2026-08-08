# Given a weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 2d array edges[][], 
# where edges[i] = [u, v, w] represents a direct edge from node u to v having w edge weight. 
# You are also given a source vertex src.

# Compute the shortest distances from the src to all other vertices. If a vertex is unreachable from the src, its 
# distance should be marked as 108. Additionally, if the graph contains a negative weight cycle, return [-1] 
# to indicate that shortest paths cannot be reliably computed.

# Examples:

# Input: V = 5, edges[][] = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], src = 0
# Output: [0, 5, 6, 6, 7]
# Explanation: Shortest Paths:
# For 0 to 1 minimum distance will be 5. By following path 0 -> 1
# For 0 to 2 minimum distance will be 6. By following path 0 -> 1 -> 2
# For 0 to 3 minimum distance will be 6. By following path 0 -> 1 -> 2 -> 4 -> 3 
# For 0 to 4 minimum distance will be 7. By following path 0 -> 1 -> 2 -> 4

# Input: V = 4, edges[][] = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], src = 0
# Output: [-1]
# Explanation: The graph contains a negative weight cycle formed by the path 1 -> 2 -> 3 -> 1, 
# where the total weight of the cycle is negative.


# Constraints:
# 1 ≤ V ≤ 100
# 1 ≤ E = edges.size() ≤ V*(V-1)
# -1000 ≤ w ≤ 1000
# 0 ≤ src < V

class Solution:

    def bellmanFord(self, V, edges, src):

        distance = [float('inf')] * V
        distance[src] = 0

        # Relax all V - 1 edges, Why V - 1, because you can atmost visit V - 1 vertices in a path
        for _ in range(V - 1):
            for edge in edges:
                source = edge[0]
                destination = edge[1]
                weight = edge[2]

                if distance[source] != float('inf') and weight + distance[source] < distance[destination]:
                    distance[destination] = weight + distance[source]

        # Perform Relaxation for one more time to detect any negative cycles
        for edge in edges:
            source = edge[0]
            destination = edge[1]
            weight = edge[2]

            if distance[source] != float('inf') and weight + distance[source] < distance[destination]:
                return [-1]

        return distance

V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0

V = 8
edges = [[1, 0, -4], [3, 5, -4], [4, 3, -5], [5, 3, -10]]
src = 1

# V = 4
# edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
# src = 0

sol_obj = Solution()
print(sol_obj.bellmanFord(V, edges, src))