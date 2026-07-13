# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted 
# in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?


class Solution():

    def squares_of_sorted_arr(self, nums):
        pivot = 0
        square_sorted_arr = []
        for index, num in enumerate(nums):
            if num >= 0:
                pivot = index
                break
        
        i = pivot - 1
        j = pivot

        while i >= 0 and j < len(nums):
            i_sq = nums[i] ** 2
            j_sq = nums[j] ** 2

            if i_sq <= j_sq:
                square_sorted_arr.append(i_sq)
                i -= 1
            else:
                square_sorted_arr.append(j_sq)
                j += 1
        print(square_sorted_arr, i, j)
        
        while i >= 0:
            square_sorted_arr.append(i_sq)
            i -= 1
        
        while j < len(nums):
            square_sorted_arr.append(j_sq)
            j += 1

        return square_sorted_arr

nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]
sol_obj = Solution()
print(sol_obj.squares_of_sorted_arr(nums))