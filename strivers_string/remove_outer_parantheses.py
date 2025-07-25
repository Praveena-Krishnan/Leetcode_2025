"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s."""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        c1=0 
        c2=0
        start=0
        for i in range(len(s)):
            if s[i]=='(':
                c1+=1
            elif s[i]==')':
                c2+=1 
            if c1==c2:
                res+=s[start+1:i]
                c1=c2=0
                start=i+1
        return res
    
    
        