# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums 
# such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.
 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution:

    def three_sum_closest(self, nums, target):
        closest_diff = float('inf')
        closest_sum = float('inf')
        nums = sorted(nums)

        for index, num in enumerate(nums):
            low = index + 1
            high = len(nums) - 1

            while low < high:
                local_sum = num + nums[low] + nums[high]
                local_sum_diff = abs(target - (local_sum))

                if local_sum_diff < closest_diff:
                    closest_diff = local_sum_diff
                    closest_sum = local_sum

                if local_sum == target:
                    return closest_sum            
                elif local_sum < target:
                    low += 1
                else:
                    high -= 1

        return closest_sum


sol_obj = Solution()
# nums = [-1,2,1,-4]
# target = 1

# nums = [0,0,0]
# target = 1

# nums = [10,20,30,40,50,60,70,80,90]
# target = 1

nums = [0,1,2]
target = 3

print(sol_obj.three_sum_closest(nums, target))
