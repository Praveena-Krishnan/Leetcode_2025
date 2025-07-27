
arr=[5,7,7,8,8,10]
n=len(arr)
ans=n

low=0
high=n-1
x=8
while low<=high:
    mid=(low+high)//2
    if arr[mid]>x:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("Upper bound of", x, "is at index:", ans)