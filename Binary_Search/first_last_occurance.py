class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums,traget):
            n=len(nums)
            lb=n
            low=0
            high=n-1
            x=traget
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=x:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb
        

        def upper_bound(nums,target):
            n=len(nums)
            ub=n

            low=0
            high=n-1
            x=target
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>x:
                    ub=mid
                    high=mid-1
                else:
                    low=mid+1
            return ub-1


        lb=lower_bound(nums,target)
        ub=upper_bound(nums,target)

        if lb==len(nums) or nums[lb]!=target:
            return [-1,-1]
        else:
            return [lb,ub]
           
                    