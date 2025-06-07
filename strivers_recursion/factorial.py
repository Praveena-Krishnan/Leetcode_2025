def factorial(n:int)->int:
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1) * n
    
if __name__ == "__main__":
    print(factorial(6))