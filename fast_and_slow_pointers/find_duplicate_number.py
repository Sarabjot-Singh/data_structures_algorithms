# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

# Input: nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
# Output: 9
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# Assumption: solution exists for a question

# creating graph for the nums (detect start of cycle using Fast and slow pointers)
#           |-----------------------------| 
#           V                             |
# 0 -> 2 -> 9 -> 1 -> 5 -> 3 -> 6 -> 8 -> 7

class Solution:

    def find_duplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]

        while True:
            if slow == fast:
                break

            slow = nums[slow]
            fast = nums[nums[fast]]

        # resestting the slow pointer
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        

nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
# nums = [3,3,3,3,3]
# nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
sol_obj = Solution()
print(sol_obj.find_duplicate(nums))