#insertion sort implementation

my_array=[12,56,42,39,2,0]

for i in range(1,len(my_array)):
    j=i-1
    while (j>=0 and my_array[j-1]>my_array[j]):
        my_array[j-1],my_array[j]=my_array[j],my_array[j-1]
        j-=1
print(my_array)