# Given an array arr[] of distinct integers and a value sum, 
# find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) 
# smaller than the given value sum.

# Examples :

# Input: sum = 2, arr[] = [-2, 0, 1, 3]
# Output:  2
# Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). 

# Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
# Output: 4
# Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).

# Constraints:
# 1 ≤ sum ≤ 105
# 3 ≤ arr.size() ≤ 103
# -103 ≤ arr[i] ≤ 103


class Solution:

    def triplet_sum_less(self, nums, target):
        if len(nums) < 3:
            return 0

        # sort the nums for two pointer algorithm
        nums = sorted(nums)
        sum_less_than_target = 0
        for index, num in enumerate(nums):
            low = index + 1
            high = len(nums) - 1

            while low < high:
                local_sum = num + nums[low] + nums[high]

                if local_sum < target:
                    sum_less_than_target += (high - low)
                    low += 1
                else:
                    high -= 1

        return sum_less_than_target

target = 2
nums = [-2, 0, 1, 3]

# target = 12
# nums = [5, 1, 3, 4, 7]

sol_obj = Solution()
print(sol_obj.triplet_sum_less(nums, target))


