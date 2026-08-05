# Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array 
# edges[][], where edges[i]=[u, v, w] represents the edge between the nodes u and v having w weight.
# Find the shortest distance of all the vertices from the source vertex src, and return an array of integers where 
# the ith element denotes the shortest distance between ith node and source vertex src.

# Note: The Graph is connected and doesn't contain any negative weight edge.
# It is guaranteed that all the shortest distance will fit in a 32-bit integer.

# Examples:

# Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
# Output: [4, 3, 0]
# Explanation:

# Shortest Paths:
# For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
# For 2 to 1 minimum distance will be 3. By following path 2 -> 1
# For 2 to 2 minimum distance will be 0. By following path 2 -> 2
# Input: V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], src = 0
# Output: [0, 4, 8, 10, 10]
# Explanation: 

# Shortest Paths: 
# For 0 to 1 minimum distance will be 4. By following path 0 -> 1
# For 0 to 2 minimum distance will be 8. By following path 0 -> 2
# For 0 to 3 minimum distance will be 10. By following path 0 -> 2 -> 3 
# For 0 to 4 minimum distance will be 10. By following path 0 -> 1 -> 4
# Constraints:
# 1 ≤ V ≤ 106
# 1 ≤ E = edges.size() ≤ 106
# 0 ≤ edges[i][0], edges[i][1] ≤ V-1
# 0 ≤ edges[i][2] ≤ 104
# 0 ≤ src < V
# edges[i]=[u, v, w]

import heapq

class Pair:

    def __init__(self, weight, vertex):
        self.weight = weight
        self.vertex = vertex

    def __lt__(self, other):
        return self.weight < other.weight 
    

class Solution:

    def dijkstra__s(self, V, edges, src):
        if V == 0:
            return float('inf')

        distance = [float('inf')] * V
        adj_list = [[] for _ in range(V)]
        heap = []

        # Creating Weighted adj_list
        for edge in edges:
            source = edge[0]
            destination = edge[1]
            weight = edge[2]

            adj_list[source].append(Pair(weight, destination))
            adj_list[destination].append(Pair(weight, source))
        
        # Initialize Source Pair and marking source distance = 0
        source_pair = Pair(0, src)
        distance[src] = 0
        heapq.heappush(heap, source_pair)

        while len(heap):
            node = heapq.heappop(heap)
            source = node.vertex
            dist = node.weight

            if dist > distance[source]:
                continue

            for neighbour in adj_list[source]:
                weight = neighbour.weight
                destination = neighbour.vertex

                if (dist + weight) < distance[destination]:
                    distance[destination] = dist + weight
                    neightbour_pair = Pair(dist + weight, destination)
                    heapq.heappush(heap, neightbour_pair)


        return distance



V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

V = 5
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0

sol_obj = Solution()
print(sol_obj.dijkstra__s(V, edges, src))