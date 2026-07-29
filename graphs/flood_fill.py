# You are given an image represented by an m x n grid of integers image, where image[i][j] represents 
# the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform 
# a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, 
# either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it 
# matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

 

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]

# Explanation:



# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

# Output: [[0,0,0],[0,0,0]]

# Explanation:

# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

 

# Constraints:

# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n


class Solution:

    def is_valid(self, row, col, n, m):
        if row < 0 or row >= n or col < 0 or col >= m:
            return False
        return True

    def dfs(self, image, visited, n, m, sr, sc, color, original_color):
        image[sr][sc] = color
        visited[sr][sc] = 1

        # helper to create neighbour indices
        row_iterator = [-1, 1, 0, 0]
        col_iterator = [0, 0, -1, 1]

        for k in range(len(row_iterator)):
            # create indices to neighbours
            row = sr + row_iterator[k]
            col = sc + col_iterator[k]

            # check if all conditions for flood fill are valid or not
            if self.is_valid(row, col, n, m) and visited[row][col] == 0 and image[row][col] == original_color:
                # perform dfs of neighbours
                self.dfs(image, visited, n, m, row, col, color, original_color)

    def flood_fill(self, image, sr, sc, color):
        n = len(image)
        m = len(image[0])

        visited = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(0)
            visited.append(row)

        original_color = image[sr][sc]

        # start dfs from image[sr][sc]
        self.dfs(image, visited, n, m, sr, sc, color, original_color)

        return image
    

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0

sol_obj = Solution()
print(sol_obj.flood_fill(image, sr, sc, color))