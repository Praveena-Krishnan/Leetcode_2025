"""Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
"""

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        ans=""
        sorted_chars=sorted(freq.keys() , key=lambda x:freq[x] , reverse=True)
        for i in sorted_chars:
            ans+=i*(freq[i])

            
        return ans