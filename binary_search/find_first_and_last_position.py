# Given an array of integers nums sorted in non-decreasing order, find the starting 
# and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:

    def find_first_occurence(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return low

    def find_last_occurence(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return high

    def first_last_position(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        low = self.find_first_occurence(nums, target)
        high = self.find_last_occurence(nums, target)

        if low > high:
            return [-1, -1]
        return [low, high]


nums = [5,7,7,7,7,7,7,7,8,8,10]
target = 7

nums = [5,7,7,8,8,10]
target = 10

sol_obj = Solution()
print(sol_obj.first_last_position(nums, target))
                