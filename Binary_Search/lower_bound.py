"""Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
Pre-requisite: Binary Search algorithm
"""

arr=[5,7,7,8,8,10]
n=len(arr)
ans=n

low=0
high=n-1
x=8
while low<=high:
    mid=(low+high)//2
    if arr[mid]<x:
        low=mid+1
    else:
        ans=mid
        high=mid-1
print("Lower bound of", x, "is at index:", ans)