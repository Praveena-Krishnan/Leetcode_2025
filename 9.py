"""
This module provides a solution to the "Palindrome Number" problem from LeetCode.

Problem Description:
A palindrome number is a number that reads the same backward as forward. For example, 121 is a palindrome, 
but 123 is not. The task is to determine whether a given integer is a palindrome.

Constraints:
- The input is an integer, which can be positive, negative, or zero.
- Negative numbers are not considered palindromes because of the leading '-' sign.

Approach:
1. Convert the integer to a string to easily reverse it and compare it with the original string.
2. Alternatively, solve the problem without converting the integer to a string by reversing the number mathematically.
3. Handle edge cases such as negative numbers and single-digit numbers.

Examples:
- Input: 121
    Output: True (121 is a palindrome)
- Input: -121
    Output: False (-121 is not a palindrome due to the negative sign)
- Input: 10
    Output: False (10 reversed is 01, which is not the same as 10)

This solution is designed to be efficient and easy to understand, adhering to the constraints and requirements of the problem.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str=str(x)
        if x_str[::-1]==x_str:
            return True
        return False
        