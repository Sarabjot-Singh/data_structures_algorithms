# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:

    def three_sum(self, nums):
        target = 0
        triplets = []
        nums = sorted(nums)
        
        for index, num in enumerate(nums):
            if index != 0 and nums[index] == nums[index - 1]:
                continue

            low = index + 1
            high = len(nums) - 1
            
            while low < high:
                local_sum = num + nums[low] + nums[high]
                
                if local_sum == target:
                    triplet = [num, nums[low], nums[high]]
                    triplets.append(triplet)

                    low += 1
                    high -= 1
                    while nums[low - 1] == nums[low]:
                        low += 1
                    while nums[high + 1] == nums[high]:
                        high -= 1
                
                elif local_sum < target:
                    low += 1
                
                else:
                    high -= 1

        return triplets


nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0]
# nums = [-2,0,0,2]
# nums = [-5,-4,-3]
sol_obj = Solution()
print(sol_obj.three_sum(nums))