"""
Problem Description:
LeetCode Problem 187 - Repeated DNA Sequences

The problem requires finding all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. The DNA string is composed of 
the characters 'A', 'C', 'G', and 'T'. 

Constraints:
- The input string's length will not exceed 10^5.
- The output should contain all the repeated sequences in any order.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

The goal is to efficiently identify these repeated sequences using 
appropriate data structures and algorithms to handle the constraints.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        seen=set()
        j=0
        n=len(s)
        while j<(n-9):
            s1=s[j:j+10]
            if s1 in seen:
                ans.add(s1)
            else:
                seen.add(s1)
            j+=1
        return list(ans)

            
        return ans


        