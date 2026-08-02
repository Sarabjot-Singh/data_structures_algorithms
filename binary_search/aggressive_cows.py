# Given an integer array arr[], which denotes the positions of stalls. All the positions are distinct. 
# There are k aggressive cows.

# Assign the cows to the stalls such that the minimum distance between any two cows is maximized.

# Examples:

# Input: arr[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. 
# The minimum distance between any two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements.
# Input: arr[] = [10, 1, 2, 7, 5], k = 3
# Output: 4
# Explanation: The first cow can be placed at arr[0], the second at arr[1], and the third at arr[4]. In this arrangement, 
# the minimum distance between any two cows is 4 (between arr[1] and arr[4]), which is the maximum possible among all valid arrangements.
# Constraints:
# 2 ≤ arr.size() ≤ 106
# 0 ≤ arr[i] ≤ 108
# 2 ≤ k ≤ arr.size()


class Solution:

    def can_place_cows(self, arr, k, distance):
        low = 0
        cows_placed = 1
        for high in range(1, len(arr)):
            if arr[high] - arr[low] >= distance:
                cows_placed += 1
                low = high
                if cows_placed == k:
                    return True

        return False
    

    def aggressiveCows(self, arr, k):
        if len(arr) <= 1 or k > len(arr):
            return -1
        
        low = 1
        high = max(arr)
        max_distance = -float('inf')
        arr = sorted(arr)

        while low <= high:
            mid = (low + high) // 2
            can_place_cows_flag = self.can_place_cows(arr, k, mid)

            if can_place_cows_flag:
                max_distance = max(max_distance, mid)
                low = mid + 1
            else:
                high = mid - 1

        return max_distance

arr = [1, 2, 4, 8, 9]
k = 3

arr = [10, 1, 2, 7, 5]
k = 3

sol_obj = Solution()
print(sol_obj.aggressiveCows(arr=arr, k=k))