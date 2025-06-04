"""problem Statement: Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder. I
n other words, if N is divisible by another integer without any remainder, then that integer is considered 
a divisor of N."""

def print_all_divisors(n: int) -> list[int]:
    ans=[]
    for i in range(1,n+1):
        if n%i==0:
            ans.append(i)
    return ans

if __name__=="__main__":
    print(print_all_divisors(10))  # Output: [1, 2,