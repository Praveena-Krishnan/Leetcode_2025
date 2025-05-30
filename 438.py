"""
LeetCode Problem 438: Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.
"""
class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26
        
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        result = []
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result