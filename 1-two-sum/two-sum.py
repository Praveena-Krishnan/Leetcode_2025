class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l1=[]
        # for i in range (len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             if i not in l1 and j not in l1:
        #                 l1.append(i)
        #                 l1.append(j) 
        # return l1
        nummap={}
        n=len(nums)
        for i in range(n):
            complement=target-nums[i]
            if complement in nummap:
                return [nummap[complement],i]
            nummap[nums[i]]=i
        return []

        

        