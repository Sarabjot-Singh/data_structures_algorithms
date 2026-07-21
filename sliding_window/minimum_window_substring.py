# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such 
# that every character in t (including duplicates) is included in the window. If there is no such substring, 
# return the empty string "".

# The testcases will be generated such that the answer is unique.
 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?


class Solution:

    def min_window_substr(self, s, t):
        t_freq_map = {}
        low = high = 0
        formed = 0
        start_end_index = [-1, -1]
        min_len = float('inf')

        for char in t:
            t_freq_map[char] = t_freq_map.get(char, 0) + 1

        while high < len(s):
            if s[high] in t_freq_map:
                t_freq_map[s[high]] -= 1
                if not t_freq_map[s[high]] < 0:
                    formed += 1

            while formed == len(t):
                if (high - low) + 1 < min_len:
                    min_len = (high - low) + 1
                    start_end_index = [low, high]
                if s[low] in t_freq_map:
                    t_freq_map[s[low]] += 1
                    if not t_freq_map[s[low]] <= 0:
                        formed -= 1
                low += 1

            high += 1

        return s[start_end_index[0]:start_end_index[1] + 1]



s = 'ADOBECODEBANC'
t = 'AABC'

# s = "a"
# t = "a"

# s = "a"
# t = "aa"
sol_obj = Solution()
print(sol_obj.min_window_substr(s, t))