my_array=[12,56,42,39,2,0]
n=len(my_array)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
print(my_array)