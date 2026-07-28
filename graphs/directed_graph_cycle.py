# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, 
# check whether it contains any cycle or not.
# The graph is represented as a 2D vector edges[][], 
# where each entry edges[i] = [u, v] denotes an edge from vertex u to v.

# Examples:

# Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]
# Output: true
# Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0


# Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Output: false
# Explanation: no cycle in the graph
# Constraints:
# 1 ≤ V ≤ 105
# 0 ≤ E ≤ 105
# 0 ≤ edges[i][0], edges[i][1] < V

class Solution:
    def dfs(self, adj_list, visited, path, node, cycle):
        visited[node] = 1
        path[node] = 1

        for neighbour in adj_list[node]:
            # check if cycle exist in the path of traversal
            if visited[neighbour] == 1 and path[neighbour] == 1:
                cycle[0] = True
                return

            # traverse as per dfs if node is not visited
            if visited[neighbour] == 0:
                self.dfs(adj_list, visited, path, neighbour, cycle)

        path[node] = 0

    def isCycle(self, edges, V):
        # create adj_list
        adj_list = [[] for _ in range(V)]

        for edge in edges:
            source = edge[0]
            destination = edge[1]

            adj_list[source].append(destination)

        visited = [0 for _ in range(V)]
        path = [0 for _ in range(V)]
        cycle = [False]

        for node in range(len(adj_list)):
            if visited[node] == 0:
                self.dfs(adj_list, visited, path, node, cycle)

        return cycle[0]


V = 4
edges= [[0, 1], [1, 2], [2, 0], [2, 3]]

V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

sol_obj = Solution()
print(sol_obj.isCycle(edges, V))