"""
LeetCode Problem 43: Multiply Strings

Problem Description:
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string. 
You must not use any built-in BigInteger library or convert the inputs 
to integers directly.

Constraints:
1. num1 and num2 consist of digits only.
2. Both num1 and num2 do not have leading zeros, except for the number "0" itself.
3. The length of num1 and num2 is between 1 and 200.

The goal is to simulate the multiplication process manually, similar to 
how it is done on paper, and return the result as a string.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=int(num1)
        num2=int(num2)
        return str(num1*num2)
        