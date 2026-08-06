# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed 
# edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes 
# for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
# If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

import heapq

class Pair:

    def __init__(self, weight, vertex):
        self.weight = weight
        self.vertex = vertex

    def __lt__(self, other):
        return self.weight < other.weight

class Solution:

    def network_delay(self, times, n, k):
        if n == 0:
            return -1

        time = [float('inf')] * n
        adj_list = [[] for _ in range(n)]
        heap = []

        for edge in times:
            source = edge[0] - 1
            destination = edge[1] - 1
            weight = edge[2]

            adj_list[source].append(Pair(weight, destination))

        # marking time for source to source = 0 and pushing source node to heap
        heapq.heappush(heap, Pair(0, k - 1))
        time[k - 1] = 0

        while len(heap):
            node = heapq.heappop(heap)
            weight = node.weight
            source = node.vertex

            if weight < time[source]:
                continue

            for neighbour in adj_list[source]:
                destination_time = neighbour.weight
                destination = neighbour.vertex

                if weight + destination_time < time[destination]:
                    time[destination] = weight + destination_time
                    heapq.heappush(heap, Pair(weight + destination_time, destination))


        max_time = max(time)
        return -1 if max_time == float('inf') else max_time

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

times = [[1,2,1]]
n = 2
k = 1

times = [[1,2,1]]
n = 2
k = 2

sol_obj = Solution()
print(sol_obj.network_delay(times, n, k))