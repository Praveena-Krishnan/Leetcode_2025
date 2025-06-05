''' Problem: Print numbers from 1 to N using recursion.

Given a positive integer N, write a recursive function to print numbers from 1 to N in increasing order. 
The function should not use any loops and must use recursion to achieve the result. '''

def print_numbers(n: int) -> None:
    if n<=0:
        return
    print_numbers(n-1)
    print(n)
    
if __name__ == "__main__":
    N = 5
    print_numbers(N)  # Output: 1 2 3 4 5
    # Note: The output will be printed in increasing order, one number per line.
    
