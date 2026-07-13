# Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s 
# onto the left side and 1s onto the right side of the array.

# Examples :

# Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].
# Input: arr[] = [1, 1]
# Output: [1, 1]
# Explanation: There are no 0s in the given array, so the modified array is [1, 1]
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 1

class Solution:
    def seg_0_and_1(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            if nums[low] == 0:
                low += 1
            elif nums[low] > nums[high]:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
            else:
                high -= 1

        return nums
            

sol_obj = Solution()
nums = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# nums = [1, 1]
# nums = [1, 0, 1]

print(sol_obj.seg_0_and_1(nums))