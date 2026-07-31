# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
# some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats 
# all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

import math

class Solution:

    def can_koko_eat_bananas(self, piles, h, speed):
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / speed)
        return hours_needed <= h

    def koko_eating_bananas(self, piles, h):
        # koko banana eating speed range
        low = 1
        high = max(piles)
        min_speed = float('inf')

        while low <= high:
            mid = (low + high) // 2

            possible_flag = self.can_koko_eat_bananas(piles, h, mid)

            if possible_flag:
                min_speed = min(min_speed, mid)
                high = mid - 1

            else:
                low = mid + 1

        return min_speed
        


piles = [3,6,7,11]
h = 8

piles = [30,11,23,4,20]
h = 5

piles = [30,11,23,4,20]
h = 6
sol_obj = Solution()
print(sol_obj.koko_eating_bananas(piles, h))