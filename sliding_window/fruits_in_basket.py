# You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) 
# while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 

# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length


class Solution:

    def fruits_in_basket(self, fruits):
        fruits_freq_map = {}
        low = high = 0
        max_fruits = 0

        while high < len(fruits):
            fruits_freq_map[fruits[high]] = fruits_freq_map.get(fruits[high], 0) + 1

            while len(fruits_freq_map) > 2:
                fruits_freq_map[fruits[low]] -= 1
                if fruits_freq_map[fruits[low]] == 0:
                    fruits_freq_map.pop(fruits[low], None)
                low += 1

            max_fruits = max(max_fruits, (high - low) + 1)

            high += 1

        return max_fruits
    
fruits = [1,2,1]
fruits = [0,1,2,2]
fruits = [1,2,3,2,2]
fruits = [1]
fruits = []
sol_obj = Solution()

print(sol_obj.fruits_in_basket(fruits))
