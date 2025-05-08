"""
LeetCode Problem 228: Summary Ranges

This problem involves finding the summary of ranges in a sorted unique integer array.
Given a sorted array of distinct integers, the task is to return the smallest sorted list of ranges 
that cover all the numbers in the array exactly. Each range should be represented as a string 
in the format "start->end" if the range contains more than one number, or as a single number 
if the range contains only one number.

For example:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Constraints:
- The input array is sorted in ascending order.
- The input array contains unique integers.
- The length of the array is between 0 and 20,000.
"""
class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = n
                end = n
        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))
        return res