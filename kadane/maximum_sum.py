# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
# which is more subtle.

class Solution:

    def max_subarray_sum(self, nums):
        if len(nums) == 0:
            return -float('inf')

        max_sum = nums[0]
        best_sum_at_i = nums[0]

        for i in range(1, len(nums)):
            best_sum_at_i = max(best_sum_at_i + nums[i], nums[i])
            max_sum = max(max_sum, best_sum_at_i)

        return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [5,4,-1,7,8]
nums = []
sol_obj = Solution()
print(sol_obj.max_subarray_sum(nums))
