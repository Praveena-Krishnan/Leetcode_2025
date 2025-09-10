from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        n=len(nums)
        ans=[]
        for i in freq:
            if freq[i]>(n/3):
                ans.append(i)
        return ans



        