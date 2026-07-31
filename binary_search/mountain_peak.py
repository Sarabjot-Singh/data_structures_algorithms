# You are given an integer mountain array arr of length n where the values increase to a 
# peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]

# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]

# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]

# Output: 1

 

# Constraints:

# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.

class Solution:

    def mountain_peak(self, nums):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if mid != len(nums) - 1 and nums[mid] <= nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return low

nums = [0,1,0]
nums = [0,2,1,0]
nums = [0,10,20,2]
sol_obj = Solution()
print(sol_obj.mountain_peak(nums))