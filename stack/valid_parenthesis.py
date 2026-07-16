# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:

    def valid_parenthesis(self, s):
        bracket_pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        opening_set = set(['(', '[', '{'])
        stack = []

        for bracket in s:
            if len(stack) and bracket not in opening_set and bracket_pairs[bracket] == stack[-1]:
                stack.pop()
                continue
            stack.append(bracket)

        return len(stack) == 0



s = "[[["

sol_obj = Solution()
print(sol_obj.valid_parenthesis(s))