# There are n cities. Some of them are connected, while some are not. If city a is connected directly with 
# city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are 
# directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution:

    def dfs(self, node, isConnected, visited, n):
        visited[node] = 1
        for vertex in range(n):
            if isConnected[node][vertex] == 1 and visited[vertex] == 0:
                self.dfs(vertex, isConnected, visited, n)


    def num_provinces(self, isConnected):
        n = len(isConnected)
        visited = [0 for _ in range(n)]
        provinces = 0

        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, isConnected, visited, n)
                provinces += 1

        return provinces

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
sol_obj = Solution()
print(sol_obj.num_provinces(isConnected=isConnected))