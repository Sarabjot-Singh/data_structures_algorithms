# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:

    def merge(self, intervals):
        merged_intervals = []
        if len(intervals) == 0:
            return merged_intervals

        if len(intervals) == 1:
            return intervals

        # sorting intervals based on the start time of each interval
        intervals = sorted(intervals)
        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if start2 <= end1:
                end1 = max(end1, end2)

            else:
                merged_intervals.append([start1, end1])
                start1 = start2
                end1 = end2

        # merging the last remaning interval
        merged_intervals.append([start1, end1])

        return merged_intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[4,7],[1,4]]
sol_obj = Solution()
print(sol_obj.merge(intervals))

