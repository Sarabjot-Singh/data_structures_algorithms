# Given a sorted array arr[] and an integer target, find the number of occurrences of target in given array.

# Examples:

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
# Output: 4
# Explanation: 2 occurs 4 times in the given array.

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
# Output: 0
# Explanation: 4 is not present in the given array.

# pattern: Binary Search->first and last occurence

class Solution:
    def find_first_occurence(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high -= 1

            else:
                low += 1

        return low

    def find_last_occurence(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low += 1
            else:
                high -= 1

        return high

    def find_number_of_occurence(self, nums, target):
        if len(nums) == 0:
            return -1

        low = self.find_first_occurence(nums, target)
        high = self.find_last_occurence(nums, target)

        return high - low + 1


nums = [1, 1, 2, 2, 2, 2, 3]
target = 2

nums = [1, 1, 2, 2, 2, 2, 3]
target = 4

sol_obj = Solution()
print(sol_obj.find_number_of_occurence(nums, target))