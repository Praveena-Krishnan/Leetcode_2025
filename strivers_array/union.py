"""Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.The union of two arrays can be defined as the common and distinct 
elements in the two arrays.
NOTE: Elements in the union should be in ascending order."""

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]

nums1 = set(nums1)
nums2 = set(nums2)

print("Union of two arrays:", sorted(nums1.union(nums2)))  # Output: Union of two arrays: [1, 2, 3, 4, 5, 7]