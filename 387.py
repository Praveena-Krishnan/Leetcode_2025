"""
Problem Description:
Given a string `s`, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

You may assume the string contains only lowercase English letters.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
- 1 <= s.length <= 10^5
- `s` consists of only lowercase English letters.
"""
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        coll=Counter(s)
        for i in coll:
            if coll[i]==1:
                return s.index(i)
        else:
            return -1
        
        
            
            
                

        