# Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], 
# where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every 
# directed edge u -> v, vertex u comes before v in the ordering.
# Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological 
# sort is correct then the output will be true else false.

# Examples:

# Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]

# Output: true
# Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
# [3, 2, 1, 0]
# [1, 2, 3, 0]
# [2, 3, 1, 0]
# Input: V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]

# Output: true
# Explanation: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
# [4, 5, 0, 1, 2, 3]
# [5, 2, 4, 0, 1, 3]

# Constraints:
# 2  ≤  V  ≤  5 x 103
# 1  ≤  E = edges.size()  ≤  min[105, (V * (V - 1)) / 2]
# 0 ≤ edges[i][0], edges[i][1] < V

from collections import deque

class Solution:

    def topological_sort(self, edges, V):
        result = []
        if V <= 0:
            return result

        adj_list = [[] for _ in range(V)]
        indegree = [0] * V
        queue = deque()

        # create adj_list and indegree
        for edge in edges:
            source = edge[0]
            destination = edge[1]

            adj_list[source].append(destination)
            indegree[destination] += 1

        # push all nodes to queue where degree = 0
        for node, degree in enumerate(indegree):
            if degree == 0:
                queue.append(node)

        if len(queue) == 0:
            print('Given graph is not a DAG')
            return result

        # perform bfs on the graph to check for neighbours and order of traversal
        while len(queue):
            node = queue.popleft()
            result.append(node)

            for neighbour in adj_list[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return result

V = 4
edges = [[3, 0], [1, 0], [2, 0]]

V = 6 
edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]

V = 2
edges = [[1, 0], [0, 1]]

sol_obj = Solution()
print(sol_obj.topological_sort(edges=edges, V=V))