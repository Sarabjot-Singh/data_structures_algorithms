# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


class Solution:

    def min_len_subarray(self, nums, target):
        min_len_subarray = float('inf')
        high = low = 0
        sumi = 0

        while high < len(nums):
            sumi += nums[high]

            while sumi >= target:
                min_len_subarray = min(min_len_subarray, (high - low) + 1)
                sumi -= nums[low]
                low += 1

            high += 1

        return min_len_subarray if min_len_subarray != float('inf') else 0


target = 7
nums = [2,3,1,2,4,3]

target = 4
nums = [1,4,4]

target = 11
nums = [1,1,1,1,1,1,1,1]

sol_obj = Solution()
print(sol_obj.min_len_subarray(nums, target))