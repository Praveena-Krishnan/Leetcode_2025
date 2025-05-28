"""
LeetCode Problem 42: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation:
The above elevation map (represented by array [0,1,0,2,1,0,1,3,2,1,2,1]) is shown as bars.
6 units of rain water (blue section) are being trapped.

Constraints:
- 1 <= height.length <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l,r=0,len(height)-1
        leftmax,rightmax=height[l],height[r]
        ans=0

        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                ans+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                ans+=rightmax-height[r]
        return ans
            

        