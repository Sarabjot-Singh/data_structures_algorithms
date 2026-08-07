# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
# where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, 
# (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 
# You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
 

# Constraints:

# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

import heapq

class Pair:

    def __init__(self, weight, row, col):
        self.weight = weight
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.weight < other.weight

class Solution:

    def is_valid(self, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        return True

    def pathWithMinimumEffort(self, heights):
        n = len(heights)
        m = len(heights[0])

        heap = []
        effort = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(float('inf'))
            effort.append(row)


        effort[0][0] = 0
        heapq.heappush(heap, Pair(0,0,0))

        row_iterator = [-1, 1, 0, 0]
        col_iterator = [0, 0, -1, 1]
        while len(heap):
            node = heapq.heappop(heap)
            weight = node.weight
            i = node.row
            j = node.col

            for k in range(len(row_iterator)):
                row = i + row_iterator[k]
                col = j + col_iterator[k]

                if not self.is_valid(row, col, n, m):
                    continue

                abs_effort_between_heights = abs(heights[i][j] - heights[row][col])
                max_effort = max(weight, abs_effort_between_heights)

                if effort[row][col] <= max_effort:
                    continue

                # if new max_effort is less than effort[row][col]
                effort[row][col] = max_effort
                heapq.heappush(heap, Pair(max_effort, row, col))

        return effort[n - 1][m - 1]



heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
sol_obj = Solution()
print(sol_obj.pathWithMinimumEffort(heights=heights))