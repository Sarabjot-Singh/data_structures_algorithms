# Given an undirected graph with V vertices and E edges, 
# represented as a 2D vector edges[][], where each entry edges[i] = [u, v] 
# denotes an edge between vertices u and v, 
# determine whether the graph contains a cycle or not.

# Note: The graph can have multiple component.

# Examples:

# Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Output: true
# Explanation: 
# 1 -> 2 -> 0 -> 1 is a cycle.

# Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
# Output: false
# Explanation:  
# No cycle in the graph.

# Constraints:
# 1 ≤ V, E ≤ 105
# 0 ≤ edges[i][0], edges[i][1] < V

class Solution:
    def dfs(self, adj_list, visited, node, parent, cycle):
        visited[node] = 1

        for neighbour in adj_list[node]:
            if visited[neighbour] == 1 and neighbour != parent:
                cycle[0] = True
                return
            if visited[neighbour] == 0:
                self.dfs(adj_list, visited, neighbour, node, cycle)


    def isCycle(self, edges, V):
        adj_list = [[] for _ in range(V)]

        # build adjacency list for undirected graph
        for edge in edges:
            source = edge[0]
            destination = edge[1]

            adj_list[source].append(destination)
            adj_list[destination].append(source)

        # build visited array for vertices
        visited = [0 for _ in range(V)]
        cycle = [False]
        for node in range(len(adj_list)):
            if visited[node] == 0:
                self.dfs(adj_list, visited, node, -1, cycle)

        return cycle[0]

V = 4
E = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

# V = 4
# E = 3
# edges = [[0, 1], [1, 2], [2, 3]]

sol_obj = Solution()
print(sol_obj.isCycle(edges=edges, V=V))
