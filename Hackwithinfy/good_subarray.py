"""_summary_
You are given an array A of length N and an 
integer k.
It is given that a subarray from l to r is considered 
good, if the number of distinct elements in that 
subarray doesn’t exceed k. Additionally, an empty 
subarray is also a good subarray and its sum is 
considered to be zero.
Find the maximum sum of a good subarray."""

nums = [1, 2, 3, 4, 5]  # Example input
k = 3  # Example value for k
freq={}

max_sum=0
cur_sum=0
l=0

for r in range(len(nums)):
    freq[nums[r]] = freq.get(nums[r], 0) + 1
    cur_sum+=nums[r]
    
while len(freq)>k:
    max_sum=max_sum-cur_sum
    freq[nums[l]]-=1
    if freq[nums[l]] == 0:
        del freq[nums[l]]
    cur_sum-=nums[l]
    l+=1
max_sum=max(max_sum, cur_sum)
print(max_sum)  # Output the maximum sum of a good subarray