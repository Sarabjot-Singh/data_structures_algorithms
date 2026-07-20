# Given a binary array nums and an integer k, return the maximum number of consecutive 1's '
# 'in the array if you can flip at most k 0's.


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

class Solution:

    def max_ones(self, nums, k):
        num_freq_map = [0, 0]
        low = high = 0
        max_len = 0

        while high < len(nums):
            num_freq_map[nums[high]] += 1
            ones_freq = num_freq_map[1]
            curr_len = (high - low) + 1

            while curr_len - ones_freq > k:
                num_freq_map[nums[low]] -= 1
                low += 1
                curr_len = (high - low) + 1
                ones_freq = num_freq_map[1]

            max_len = max(max_len, curr_len)

            high += 1

        return max_len
    
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

nums = [0]
k = 0

sol_obj = Solution()
print(sol_obj.max_ones(nums, k))