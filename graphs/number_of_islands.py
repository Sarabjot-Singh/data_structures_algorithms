# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


class Solution:

    def is_valid_land(self, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        return True
    
    def explore_land(self, i, j, grid, visited, n, m):
        # top->bottom->left->right
        row_iterator = [-1, 1, 0, 0]
        col_iterator = [0, 0, -1, 1]
        visited[i][j] = 1

        for k in range(4):
            row = i + row_iterator[k]
            col = j + col_iterator[k]

            if self.is_valid_land(row, col, n, m) and grid[row][col] == '1' and visited[row][col] == 0:
                self.explore_land(row, col, grid, visited, n, m)

    def number_of_islands(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = []
        islands = 0

        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(0)
            visited.append(row)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.explore_land(i, j, grid, visited, n, m)
                    islands += 1

        return islands

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol_obj = Solution()
print(sol_obj.number_of_islands(grid))