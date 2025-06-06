"""
LeetCode Problem 13: Roman to Integer

This function converts a Roman numeral string into its corresponding integer value.
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, 
with the following values:

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

In Roman numerals, smaller numbers preceding larger numbers indicate subtraction, 
while smaller numbers following larger numbers indicate addition. For example:
    - "IV" represents 4 (5 - 1).
    - "IX" represents 9 (10 - 1).
    - "LVIII" represents 58 (50 + 5 + 3).
    - "MCMXCIV" represents 1994 (1000 + 900 + 90 + 4).

The function processes the Roman numeral string from left to right, applying the 
appropriate addition or subtraction rules to compute the total integer value.

Constraints:
- The input is guaranteed to be a valid Roman numeral within the range 1 to 3999.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        #largest to smallest:add them
        #smaller before larger : substract the smaller 
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0

        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                res-=roman[s[i]]
            else:
                res+=roman[s[i]]
        return res
    
if __name__ == "__main__":
    solution=Solution()