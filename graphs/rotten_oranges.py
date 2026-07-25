# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.


# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0. 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from collections import deque

class Solution:

    def is_valid(self, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        return True

    def rotten_oranges(self, grid):
        n = len(grid)
        m = len(grid[0])
        minute = 0
        queue = deque()
        fresh = 0
        row_iterator = [-1, 1, 0, 0]
        col_iterator = [0, 0, -1, 1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    queue.append([i,j])


        while len(queue) and fresh > 0:
            minute += 1
            len_queue = len(queue)

            while len_queue:
                node = queue.popleft()
                i = node[0]
                j = node[1]

                for k in range(4):
                    row = i + row_iterator[k]
                    col = j + col_iterator[k]

                    if self.is_valid(row, col, n, m) and grid[row][col] == 1:
                        queue.append([row, col])
                        grid[row][col] = 2
                        fresh -= 1

                len_queue -= 1

        return -1 if fresh > 0 else minute


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
sol_obj = Solution()
print(sol_obj.rotten_oranges(grid))

