def reverse_array(arr,l,r):
    if l==r:
        return arr
    else:
        arr[l],arr[r]=arr[r],arr[l]
        return reverse_array(arr,l+1,r-1)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    l = 0
    r = len(arr) - 1    
    reversed_arr = reverse_array(arr, l, r)
    print(reversed_arr)  # Output: [5, 4, 3, 2, 1]