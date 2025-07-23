my_array=[12,56,42,39,2,0]
largest=my_array[0]
second_largest=-1
for i in range(0,len(my_array)):
    if my_array[i]>largest:
        largest=my_array[i]

for i in range(0,len(my_array)):
    if my_array[i]>second_largest and my_array[i]!=largest:
        second_largest=my_array[i]

print("largest=",largest)
print("second largest",second_largest)
