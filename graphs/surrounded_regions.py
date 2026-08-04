# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. 
# Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
# You do not need to return anything.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


class Solution:

    def is_valid(self, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        return True


    def dfs(self, board, i, j, n, m):
        board[i][j] = '#'
        row_iterator = [-1, 1, 0, 0]
        col_iterator = [0, 0, -1, 1]

        for k in range(4):
            row = i + row_iterator[k]
            col = j + col_iterator[k]

            if self.is_valid(row, col, n, m) and board[row][col] == 'O':
                self.dfs(board, row, col, n, m)


    def surronded_regions(self, board):
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j, n, m)

        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        return board

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["X"]]
board = [["X","X","X"],["X","O","X"],["X","X","X"]]
sol_obj = Solution()
print(sol_obj.surronded_regions(board))