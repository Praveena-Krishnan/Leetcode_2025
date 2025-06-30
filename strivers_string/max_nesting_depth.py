"""Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the 
maximum number of nested parentheses.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        curr=0
        for c in s:
            if c=='(':
                curr+=1
            elif c==")":
                curr-=1
            res=max(res,curr)
        return res
        