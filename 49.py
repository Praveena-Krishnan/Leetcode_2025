"""
LeetCode Problem 49: Group Anagrams

This problem requires grouping a list of strings into anagrams. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Given an array of strings `strs`, the task is to group the strings that are anagrams of each other. 
Each group of anagrams should be returned as a list, and the result should be a list of these groups.

Constraints:
- All inputs are lowercase letters.
- The order of the output does not matter.

Example:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)

        for s in strs:
            key="".join(sorted(s))
            ans[key].append(s)
        return list(ans.values())
        


      
                    

        