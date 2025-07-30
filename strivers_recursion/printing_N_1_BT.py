"""to print numbers from N to 1 using recursion backtracking.
"""

def printing(i,n):
    if i<1:
        return
    
    print(i,end='')
    printing(i-1,n)
    
    
printing(5,5)  # Example usage, prints: 54321