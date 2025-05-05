"""
LeetCode Problem 125: Valid Palindrome

This function determines whether a given string is a valid palindrome.
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
ignoring case, spaces, and non-alphanumeric characters.

The function processes the input string by:
1. Removing all non-alphanumeric characters.
2. Converting all letters to lowercase.
3. Checking if the processed string reads the same backward as forward.

Parameters:
    s (str): The input string to be checked.

Returns:
    bool: True if the input string is a valid palindrome, False otherwise.

Constraints:
- The input string consists of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1=list(s)
        filtered=[]
        for i in l1:
            if i.isalnum():
                filtered.append(i.lower())
        s2=("".join(filtered))
        if s==" ":
            return True
        elif s2==s2[::-1]:
            return True
        else :
            return False
        
        


        