# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) 
# with at most one element deletion. In other words, you want to choose a subarray and optionally 
# delete one element from it so that there is still at least one element left and the sum of the 
# remaining elements is maximum possible.

# Note that the subarray needs to be non-empty after deleting one element.

 

# Example 1:

# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
# Example 2:

# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.
# Example 3:

# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

# Constraints:

# 1 <= arr.length <= 105
# -104 <= arr[i] <= 104


class Solution:

    def maximum_subarray_sum_one_deletion(self, nums):
        if len(nums) == 0:
            return -float('inf')

        one_delete = -float('inf')
        none_delete = nums[0]
        max_sum = none_delete

        for i in range(1, len(nums)):
            one_delete = max(one_delete + nums[i], none_delete)
            none_delete = max(none_delete + nums[i], nums[i])

            max_sum = max(max_sum, one_delete, none_delete)

        return max_sum

nums = [1,-2,0,3]
nums = [1,-2,-2,3]
nums = [-1,-1,-1,-1]
nums = [1,-1,2,3]

sol_obj = Solution()
print(sol_obj.maximum_subarray_sum_one_deletion(nums))

