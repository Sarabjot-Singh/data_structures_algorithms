# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

class Solution:

    def maximumLengthSubstring(self, s):
        if len(s) < 2:
            return -1

        char_freq_map = {}
        low = high = 0
        max_len = -float('inf')

        while high < len(s):
            char_freq_map[s[high]] = char_freq_map.get(s[high], 0) + 1

            while char_freq_map[s[high]] > 2:
                char_freq_map[s[low]] -= 1
                low += 1

            max_len = max(max_len, high - low + 1)
            high += 1

        return max_len


s = "bcbbbcba"
s = "aaaa"
sol_obj = Solution()
print(sol_obj.maximumLengthSubstring(s))
        