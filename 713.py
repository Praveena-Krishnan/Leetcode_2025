"""
Problem Description:
LeetCode 713 - Subarray Product Less Than K

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays 
where the product of all the elements in the subarray is strictly less than `k`.

Constraints:
1. 1 <= nums.length <= 3 * 10^4
2. 1 <= nums[i] <= 1000
3. 0 <= k <= 10^6

The problem requires an efficient solution, as the input size can be large. A brute-force approach 
that checks all possible subarrays may not work within the time limits. Instead, a sliding window 
or two-pointer technique is typically used to solve this problem in O(n) time complexity.
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans=0
        j=0
        i=0
        prod=1
        while j<len(nums):
            prod*=nums[j]
            while(prod>=k and i<=j):#increament i when prod >k 
                prod/=nums[i]
                i+=1
            ans+=j-i+1
            j+=1
        return ans
        

        