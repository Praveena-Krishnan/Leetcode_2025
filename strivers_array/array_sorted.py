nums = [3,4,5,1,2]
count,n=0,len(nums)
for i in range(n):
    if nums[i]>(nums[(i+1)%n]):
        count+=1
if count==1:
    print('True')
else:
    print('False')