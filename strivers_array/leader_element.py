nums = [1, 2, 5, 3, 1, 2]
leader=[]
for i in range(len(nums)):
      if i == len(nums) - 1 or nums[i] > max(nums[i+1:]):
        leader.append(nums[i])
print(leader)