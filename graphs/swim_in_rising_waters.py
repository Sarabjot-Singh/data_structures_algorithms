# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal 
# to t is submerged or reachable.

# You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually 
# are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

# Example 1:


# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# Example 2:


# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# Each value grid[i][j] is unique.


class Solution:

    def is_valid(self, i, j,m ,n):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        return True

    def dfs(self, graph, visited, i, j, n, m, level, flag):
        if i == n - 1 and j == m - 1:
            flag[0] = True
            return

        visited[i][j] = 1
        row_iterator = [-1, 1, 0, 0]
        col_iterator = [0, 0, -1, 1]

        for k in range(4):
            row = i + row_iterator[k]
            col = j + col_iterator[k]

            if self.is_valid(row, col, n, m) and  visited[row][col] == 0 and graph[row][col] <= level:
                self.dfs(graph, visited, row, col, n, m, level, flag)


    def can_swim(self, graph, level):
        n = len(graph)
        m = len(graph[0])
        flag = [False]

        visited = [[0 for _ in range(m)] for _ in range(n)]

        self.dfs(graph, visited, 0, 0, n, m, level, flag)

        return flag[0]


    def swim_in_water(self, graph):
        low = 0
        high = len(graph) * len(graph[0]) - 1
        min_level = float('inf')

        while low <= high:
            mid = (low + high) // 2
            flag = self.can_swim(graph, mid)

            if flag:
                min_level = min(min_level, mid)
                high = mid - 1

            else:
                low = mid + 1

        return min_level

grid = [[0,2],[1,3]]
# grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
sol_obj = Solution()
print(sol_obj.swim_in_water(grid))


 