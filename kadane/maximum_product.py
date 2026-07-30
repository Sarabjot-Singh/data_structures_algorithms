# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


class Solution:

    def max_product(self, nums):
        if len(nums) == 0:
            return -float('inf')
        
        best_max_at_i = nums[0]
        best_min_at_i = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = best_max_at_i * nums[i]
            v3 = best_min_at_i * nums[i]

            max_prod = max(max_prod, v1, v2, v3)

            best_max_at_i = max(v1, v2, v3)
            best_min_at_i = min(v1, v2, v3)

        return max_prod


nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [-2,3,-4]
# nums = [-1,-2,-9,-6]

sol_obj = Solution()
print(sol_obj.max_product(nums))
