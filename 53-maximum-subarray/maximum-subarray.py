class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxend=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):
            maxend=max(maxend+nums[i],nums[i])
            res=max(maxend,res)
        return res
            