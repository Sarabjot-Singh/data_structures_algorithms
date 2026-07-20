# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:

    def longest_substring_without_duplicate_characters(self, s):
        char_freq_map = {}
        low = high = 0
        max_len = 0

        while high < len(s):
            char_freq_map[s[high]] = char_freq_map.get(s[high], 0) + 1

            while char_freq_map[s[high]] > 1:
                char_freq_map[s[low]] -= 1
                low += 1

            max_len = max(max_len, (high - low) + 1)

            high += 1

        return max_len
    
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
sol_obj = Solution()
print(sol_obj.longest_substring_without_duplicate_characters(s))
            