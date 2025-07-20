from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        freq=Counter(s)
        ans=max(freq.values())-min(freq.values())
        return ans
        
        
        