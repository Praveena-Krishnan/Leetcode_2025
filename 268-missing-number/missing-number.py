class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # arr1 = [-1] * (n + 1)  
        
        # for j in nums:  # Only one loop is needed
        #     arr1[j] = 0  # Mark the number as present
        
        # return arr1.index(-1)  # The missing number is the one that remains -1

        s1=n*(n+1)//2
        s2=sum(nums)
        return (s1-s2)


        
                

        