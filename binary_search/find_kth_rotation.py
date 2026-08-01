# Find Kth Rotation

# Given an increasing sorted rotated array arr[] of distinct integers. The array is right-rotated k times. 
# Find the value of k.
# Let's suppose we have an array arr[] = [2, 4, 6, 9], if we rotate it by 2 times it will look like this:
# After 1st Rotation : [9, 2, 4, 6]
# After 2nd Rotation : [6, 9, 2, 4]

# Examples:

# Input: arr[] = [5, 1, 2, 3, 4]
# Output: 1
# Explanation: The given array is [5, 1, 2, 3, 4]. The original sorted array is [1, 2, 3, 4, 5]. We can see that the array was rotated 1 times to the right.
# Input: arr = [1, 2, 3, 4, 5]
# Output: 0
# Explanation: The given array is not rotated.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 107

class Solution:

    def find_kth_rotation(self, nums):
        if len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= nums[low] and nums[mid] > nums[high]:
                low = mid + 1
            else:
                if mid != 0 and nums[mid - 1] < nums[mid]:
                    high = mid - 1
                else:
                    return mid

nums = [5, 1, 2, 3, 4]
nums = [1, 2, 3, 4, 5]
sol_obj = Solution()
print(sol_obj.find_kth_rotation(nums))