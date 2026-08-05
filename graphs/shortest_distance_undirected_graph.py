# Shortest Path in Unweighted Graph
# Solved
# Difficulty: MediumAccuracy: 49.98%Submissions: 202K+Points: 4Average Time: 20m
# Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, where edges[i] = [u, v] 
# denotes an undirected edge between vertex u and vertex v, given two vertices src and dest, 
# find the length of the shortest path from src to dest. If there is no path between src and dest, return -1.

# Note: All edges have a unit weight of 1.

# Examples :

# Input: V = 9, edges[][] = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
# , src = 0, dest = 8
# Output: 4
# Explanation: One of the shortest paths from vertex 0 to vertex 8 is 0 -> 1 -> 2 -> 6 -> 8, which contains 4 edges.

# Input: V = 4, edges[][]= [[0, 3], [1, 3]], src = 3, dest = 2
# Output: -1
# Explanation: There is no path between vertices 3 and 2.

# Constraints:

# 1 ≤ V ≤ 10^4
# 0 ≤ E ≤ V × (V - 1) / 2
# 0 ≤ edges[i][0], edges[i][1] < V


from collections import deque

class Solution:

    def bfs(self, adj_list, visited, src, dest):
        queue = deque()
        queue.append([src, 0])

        while len(queue):
            node = queue.popleft()
            vertex = node[0]
            distance = node[1]

            visited[vertex] = 1

            if vertex == dest:
                return distance

            for neighbour in adj_list[vertex]:
                if not visited[neighbour]:
                    queue.append([neighbour, distance + 1])

        # if dest was not found while traversal that means it's not reachable
        return -1


    def shortest_path(self, V, edges, src, dest):
        if V == 0:
            return -1
        
        visited = [0] * V
        adj_list = [[] for _ in range(V)]

        # creating adj_list for undirected graph
        for edge in edges:
            source = edge[0]
            destination = edge[1]

            adj_list[source].append(destination)
            adj_list[destination].append(source)


        distance = self.bfs(adj_list, visited, src, dest)

        return distance

V = 9
edges= [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
src = 0
dest = 8

V = 4
edges = [[0, 3], [1, 3]]
src = 3
dest = 2

sol_obj = Solution()
print(sol_obj.shortest_path(V, edges, src, dest))