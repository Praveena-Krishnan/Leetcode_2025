"""
Problem 12: Integer to Roman

Given an integer, convert it to a Roman numeral. Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.

Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five, we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, return its Roman numeral representation as a string.

Constraints:
- 1 <= num <= 3999
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],
            [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
        ]
        res=""
        
        for val,sym in value_symbols:
            if num//val:
                count=num//val
                res+=(count*sym)
                num=num%val
        return res
        