# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [3,-4, 2,-3,-1, 7,-5]
# Output: -6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# nums = [2, 6, 8, 1, 4]
# Output: 1
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:

    def min_subarray_sum(self, nums):
        if len(nums) == 0:
            return float('inf')

        min_sum = nums[0]
        best_min_at_i = nums[0]

        for i in range(1, len(nums)):
            best_min_at_i = min(best_min_at_i + nums[i], nums[i])
            min_sum = min(min_sum, best_min_at_i)

        return min_sum


nums = [3,-4, 2,-3,-1, 7,-5]
nums = [2, 6, 8, 1, 4]
sol_obj = Solution()
print(sol_obj.min_subarray_sum(nums))