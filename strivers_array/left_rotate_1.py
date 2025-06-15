nums=[12,56,42,39,2,0]
n=len(nums)
temp=nums[0]
for i in range(1,n):
    nums[i-1]=nums[i]
    nums[n-1]=temp
print(nums)