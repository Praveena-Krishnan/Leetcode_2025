""" sum of first N numbers using recursion
Problem Statement: Given a positive integer N, write a recursive function 
to calculate the sum of the first N natural numbers."""

def sum_n(n)-> int:
    sum=0
    if n==0:
        return 0
    else:
        sum=n+sum_n(n-1)
        
    return sum
if __name__ == "__main__":
    n = 5
    result = sum_n(n)
    print(f"The sum of the first {n} natural numbers is: {result}")  # Output: 15
    