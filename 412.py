"""
LeetCode Problem 412: Fizz Buzz

This function solves the Fizz Buzz problem, a classic programming challenge.
The task is to generate a list of strings representing numbers from 1 to n, 
but with the following conditions:
- For multiples of 3, the string "Fizz" is added instead of the number.
- For multiples of 5, the string "Buzz" is added instead of the number.
- For numbers that are multiples of both 3 and 5, the string "FizzBuzz" is added.

Parameters:
- n (int): The upper limit of the range (inclusive).

Returns:
- List[str]: A list of strings where each element corresponds to the Fizz Buzz 
    transformation of the numbers from 1 to n.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,n+1)]
        
        
        