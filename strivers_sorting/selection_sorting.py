my_array=[12,56,42,39,2,0]

for i in range(len(my_array)):
    min=my_array[i]
    for j in range(i+1,len(my_array)):
        if my_array[j]<min:
            min=my_array[j]
            index=j
            my_array[i],my_array[index]=my_array[index],my_array[i]
print(my_array)