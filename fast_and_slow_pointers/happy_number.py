# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# Example 2:

# Input: n = 2
# Output: false

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.linklist import LinkList

class Solution:

    def sum_of_square(self, n):
        sq_sum = 0
        while n != 0:
            rem = n % 10
            n = n // 10
            sq_sum += rem ** 2

        return sq_sum

    def happy_number(self, n):
        slow = self.sum_of_square(n)
        fast = self.sum_of_square(self.sum_of_square(n))

        while True:
            if slow == fast == 1:
                return True
            
            if slow == fast != 1:
                break
            
            slow = self.sum_of_square(slow)
            fast = self.sum_of_square(self.sum_of_square(fast))

        return False

n = 19
sol_obj = Solution()
print(sol_obj.happy_number(n))